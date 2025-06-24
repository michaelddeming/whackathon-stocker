{
  description = "flake using uv2nix with Docker image";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

    pyproject-nix = {
      url = "github:pyproject-nix/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    uv2nix = {
      url = "github:pyproject-nix/uv2nix";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    pyproject-build-systems = {
      url = "github:pyproject-nix/build-system-pkgs";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.uv2nix.follows = "uv2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    inputs@{
      self,
      nixpkgs,
      uv2nix,
      pyproject-nix,
      pyproject-build-systems,
      ...
    }:
    let
      forAllSystems =
        perSystemPkgsFunction:
        nixpkgs.lib.genAttrs
          [
            "x86_64-linux"
            "aarch64-linux"
            "x86_64-darwin"
            "aarch64-darwin"
          ]
          (
            system:
            perSystemPkgsFunction (
              import nixpkgs {
                inherit system;
                config.allowUnfree = true;
              }
            )
          );

      buildOutputsForSystem =
        pkgs:
        let
          inherit (pkgs) lib;

          parsedPyprojectToml = builtins.fromTOML (builtins.readFile ./pyproject.toml);
          projectName = parsedPyprojectToml.project.name;
          requiredPythonFromToml = parsedPyprojectToml.project."requires-python" or ">=3.8";
          extractedPythonVersion =
            lib.elemAt (lib.splitString "." (lib.elemAt (lib.splitString ">=" requiredPythonFromToml) 1)) 0
            + "."
            + lib.elemAt (lib.splitString "." (lib.elemAt (lib.splitString ">=" requiredPythonFromToml) 1)) 1;

          workspace = uv2nix.lib.workspace.loadWorkspace { workspaceRoot = ./.; };
          overlay = workspace.mkPyprojectOverlay { sourcePreference = "wheel"; };
          pyprojectOverrides = _final: _prev: {
            # Build fixups for specific packages if needed.
          };

          pythonVersionPackageName = "python${builtins.replaceStrings [ "." ] [ "" ] extractedPythonVersion}";

          selectedPython =
            if pkgs ? "${pythonVersionPackageName}" && pkgs."${pythonVersionPackageName}" != null then
              pkgs."${pythonVersionPackageName}"
            else if
              pkgs ? python3
              && pkgs.python3 != null
              && lib.versionAtLeast pkgs.python3.version extractedPythonVersion
            then
              pkgs.python3
            else
              pkgs.python311;

          python = selectedPython;

          pythonSet = (pkgs.callPackage pyproject-nix.build.packages { inherit python; }).overrideScope (
            lib.composeManyExtensions [
              pyproject-build-systems.overlays.default
              overlay
              pyprojectOverrides
            ]
          );

          defaultDepSpecs = workspace.depSpecs.default or { };
          externalDepNames = lib.attrNames defaultDepSpecs;

          allPackageNamesForVenv = externalDepNames ++ [ projectName ];

          specForProductionVenv = lib.listToAttrs (
            map (name: lib.nameValuePair name [ ]) allPackageNamesForVenv
          );

          defaultPackage = pythonSet.mkVirtualEnv "stocker-env" specForProductionVenv;

          dockerImage = pkgs.dockerTools.buildImage {
            name = projectName;
            tag = "latest";
            copyToRoot = pkgs.buildEnv {
              name = "${projectName}-rootfs";
              paths = [
                defaultPackage
                pkgs.busybox
              ];
            };
            config = {
              Cmd = [ "/bin/${projectName}" ];
              WorkingDir = "/";
            };
          };

        in
        {
          packages = {
            inherit defaultPackage;
            inherit dockerImage;
          };
          apps = {
            default = {
              type = "app";
              program = "${defaultPackage}/bin/${projectName}";
            };
          };
          devShells = {
            impure = pkgs.mkShell {
              packages = [
                python
                pkgs.uv
                pkgs.pyright
              ];
              env =
                {
                  UV_PYTHON_DOWNLOADS = "never";
                  UV_PYTHON = python.interpreter;
                }
                // lib.optionalAttrs pkgs.stdenv.isLinux {
                  LD_LIBRARY_PATH = lib.makeLibraryPath pkgs.pythonManylinuxPackages.manylinux1;
                };
              shellHook = ''
                unset PYTHONPATH
              '';
            };
            default =
              let
                editableOverlay = workspace.mkEditablePyprojectOverlay {
                  root = "$REPO_ROOT";
                };
                editablePythonSet = pythonSet.overrideScope (
                  lib.composeManyExtensions [
                    editableOverlay
                    (final: prev: {
                      "${projectName}" = prev."${projectName}".overridePythonAttrs (old: {
                        # Example: add dev-specific build inputs or patches
                        # nativeBuildInputs = old.nativeBuildInputs ++ [ someDevTool ];
                      });
                    })
                  ]
                );

                allDepSpecsForDev = workspace.depSpecs.all or { };
                allExternalDepNamesForDev = lib.attrNames allDepSpecsForDev;
                allPackageNamesForDevVenv = allExternalDepNamesForDev ++ [ projectName ];

                specForDevVenv = lib.listToAttrs (map (name: lib.nameValuePair name [ ]) allPackageNamesForDevVenv);

                virtualenv = editablePythonSet.mkVirtualEnv "${projectName}-dev-env" specForDevVenv;
              in
              pkgs.mkShell {
                packages = [
                  virtualenv
                  pkgs.uv
                  pkgs.pyright
                ];
                env = {
                  UV_NO_SYNC = "1";
                  UV_PYTHON = "${virtualenv}/bin/python";
                  UV_PYTHON_DOWNLOADS = "never";
                };
                shellHook = ''
                  unset PYTHONPATH
                  export REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || echo "$PWD")
                  echo "Dev environment for ${projectName} loaded."
                  echo "Python available at: ${virtualenv}/bin/python"
                '';
              };
          };
        };

      allSystemOutputs = forAllSystems buildOutputsForSystem;

    in
    {
      packages = nixpkgs.lib.mapAttrs (
        systemName: perSystemAttrs: perSystemAttrs.packages
      ) allSystemOutputs;
      apps = nixpkgs.lib.mapAttrs (systemName: perSystemAttrs: perSystemAttrs.apps) allSystemOutputs;
      devShells = nixpkgs.lib.mapAttrs (
        systemName: perSystemAttrs: perSystemAttrs.devShells
      ) allSystemOutputs;
      defaultPackage = nixpkgs.lib.mapAttrs (
        systemName: perSystemAttrs: perSystemAttrs.packages.defaultPackage
      ) allSystemOutputs;
    };
}
