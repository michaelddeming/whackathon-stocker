{
  description = "flake using uv2nix";

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
                config.allowUnfree = true; # As per the requested structure; adjust if needed
                # overlays = []; # Add global overlays for pkgs here if needed.
                # The original flake didn't have global overlays for pkgs.
              }
            )
          );

      # This function defines all outputs for a single system.
      # It takes 'pkgs' (which is system-specific) as an argument.
      buildOutputsForSystem =
        pkgs:
        let
          inherit (pkgs) lib; # lib from the system-specific pkgs

          # Load a uv workspace from a workspace root.
          # Uv2nix treats all uv projects as workspace projects.
          workspace = uv2nix.lib.workspace.loadWorkspace { workspaceRoot = ./.; };

          # Create package overlay from workspace.
          overlay = workspace.mkPyprojectOverlay {
            # Prefer prebuilt binary wheels as a package source.
            sourcePreference = "wheel"; # or sourcePreference = "sdist";
            # Optionally customise PEP 508 environment
            # environ = {
            #   platform_release = "5.10.65";
            # };
          };

          # Extend generated overlay with build fixups
          pyprojectOverrides = _final: _prev: {
            # Implement build fixups here.
            # Note that uv2nix is _not_ using Nixpkgs buildPythonPackage.
            # It's using https://pyproject-nix.github.io/pyproject.nix/build.html
          };

          # Use Python 3 from the system-specific pkgs
          python = pkgs.python3;

          # Construct package set
          pythonSet =
            # Use base package set from pyproject.nix builders
            (pkgs.callPackage pyproject-nix.build.packages {
              inherit python;
            }).overrideScope
              (
                lib.composeManyExtensions [
                  pyproject-build-systems.overlays.default
                  overlay
                  pyprojectOverrides
                ]
              );

          # Package a virtual environment as our main application.
          # Enable no optional dependencies for production build.
          defaultPackage = pythonSet.mkVirtualEnv "stocker-env" workspace.deps.default;

        in
        {
          # Package for the current system.
          packages = {
            default = defaultPackage;
          };

          # Make stocker runnable with `nix run`
          apps = {
            default = {
              type = "app";
              program = "${defaultPackage}/bin/stocker";
            };
          };

          # Development shells
          devShells = {
            # Impurely using uv to manage virtual environments
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

            # Pure development using uv2nix
            default =
              let
                editableOverlay = workspace.mkEditablePyprojectOverlay {
                  root = "$REPO_ROOT";
                  # Optional: Only enable editable for these packages
                  # members = [ "stocker" ];
                };

                editablePythonSet = pythonSet.overrideScope (
                  lib.composeManyExtensions [
                    editableOverlay
                    (final: prev: {
                      stocker = prev.stocker.overrideAttrs (old: {
                        src = lib.fileset.toSource {
                          root = old.src;
                          fileset = lib.fileset.unions [
                            (old.src + "/pyproject.toml")
                            (old.src + "/README.md")
                            (old.src + "/src")
                          ];
                        };
                        nativeBuildInputs =
                          old.nativeBuildInputs
                          ++ final.resolveBuildSystem {
                            editables = [ ];
                          };
                      });
                    })
                  ]
                );

                virtualenv = editablePythonSet.mkVirtualEnv "stocker-dev-env" workspace.deps.all;
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
                  export REPO_ROOT=$(git rev-parse --show-toplevel)
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

      # You can also expose other top-level attributes if needed, e.g.:
      # formatter = forAllSystems (pkgs: pkgs.alejandra);
    };
}
