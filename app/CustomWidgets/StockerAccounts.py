import customtkinter as ctk
from CTkTable import *


class StockerAccounts(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.pack_propagate(False)

        # Accounts Frame Left Section
        self.StockerAccountsLeftFrame = ctk.CTkFrame(
            master=self, width=400, border_width=1
        )
        self.StockerAccountsLeftFrame.pack_propagate(False)
        self.StockerAccountsLeftFrame.grid_propagate(False)
        self.StockerAccountsLeftFrame.pack(
            side="left", fill="y", padx=(15, 7.5), pady=(5, 15)
        )

        self.StockerAccountsLeftFrame.columnconfigure(0, weight=1)
        self.StockerAccountsLeftFrame.columnconfigure(1, weight=1)

        self.StockerAccountsLeftFrame.rowconfigure(0, weight=1)  # Accounts Title
        self.StockerAccountsLeftFrame.rowconfigure(
            1, weight=1
        )  # View Account(s) Label + Accounts Drop Down
        self.StockerAccountsLeftFrame.rowconfigure(
            2, weight=1
        )  # View Account(s) Submit Button
        self.StockerAccountsLeftFrame.rowconfigure(
            3, weight=1
        )  # View Account(s) Submit Status Label
        self.StockerAccountsLeftFrame.rowconfigure(4, weight=1)  # Blank Space
        self.StockerAccountsLeftFrame.rowconfigure(5, weight=1)  # Positions Title
        self.StockerAccountsLeftFrame.rowconfigure(
            6, weight=1
        )  # Search Position(s) Label + Textbox
        self.StockerAccountsLeftFrame.rowconfigure(
            7, weight=1
        )  # Search Positions Submit Button
        self.StockerAccountsLeftFrame.rowconfigure(
            8, weight=1
        )  # Search Positions Submit Status Label

        # <-------------------------- ACCOUNT SELECT DROPDOWN MENU -------------------------->

        # TITLE: "Accounts"
        self.accounts_left_frame_title_label = ctk.CTkLabel(
            self.StockerAccountsLeftFrame, text=f"Accounts", fg_color="transparent"
        ).grid(row=0, column=0, columnspan=2)

        # ACCOUNT SELECT DROPDOWN | DROPDOWN LABEL: "Select Account(s)"
        self.select_accounts_dropdown_dropdown_label = ctk.CTkLabel(
            self.StockerAccountsLeftFrame,
            text=f"Select Account(s)",
            fg_color="transparent",
        ).grid(row=1, column=0)

        # ACCOUNT SELECT DROPDOWN | DROPDOWN-BOX: Account Names
        self.account_names = ["Roth IRA", "Taxable Account", "Traditional 401k", "all"]
        self.select_accounts_dropdown_dropdown = ctk.CTkComboBox(
            master=self.StockerAccountsLeftFrame, values=self.account_names
        ).grid(row=1, column=1)

        # ACCOUNT SELECT DROPDOWN | SUBMIT BUTTON: "View Account(s)"
        self.submit_account_view_button = ctk.CTkButton(
            master=self.StockerAccountsLeftFrame, text="View Account(s)"
        ).grid(row=2, column=0, columnspan=2)

        # ACCOUNT SELECT DROPDOWN | STATUS LABEL: "Select Account(s)"
        self.account_dropdown_status_message = "N/A"
        self.select_accounts_dropdown_status_label = ctk.CTkLabel(
            self.StockerAccountsLeftFrame,
            text=f"Status: {self.account_dropdown_status_message}",
            fg_color="transparent",
        ).grid(row=3, column=0, columnspan=2)

        # <-------------------------- POSITION SEARCH MENU -------------------------->

        # POSITION SEARCH MENU | TITLE: "Positions"
        self.positions_search_menu_title_label = ctk.CTkLabel(
            self.StockerAccountsLeftFrame, text=f"Positions", fg_color="transparent"
        ).grid(row=5, column=0, columnspan=2)

        # POSITION SEARCH MENU | POSITION SEARCHBOX LABEL: "Search Position(s)"
        self.positions_search_searchbox_label = ctk.CTkLabel(
            self.StockerAccountsLeftFrame,
            text=f"Search Position(s)",
            fg_color="transparent",
        ).grid(row=6, column=0)

        # POSITION SEARCH MENU | POSITION SEARCHBOX: "Ticker"
        self.positions_search_searchbox = ctk.CTkEntry(
            master=self.StockerAccountsLeftFrame, placeholder_text="Ticker (AAPL)"
        ).grid(row=6, column=1)

        # POSITION SEARCH MENU | POSITION SEARCH SUBMIT BUTTON: "Search Position(s)"
        self.positions_search_submit_button = ctk.CTkButton(
            master=self.StockerAccountsLeftFrame, text="Search Position(s)"
        ).grid(row=7, column=0, columnspan=2)

        # POSITION SEARCH MENU | POSITION SEARCH SUBMIT STATUS LABEL: "Status: ..."
        self.positions_search_status_message = "N/A"
        self.position_search_status_label = ctk.CTkLabel(
            self.StockerAccountsLeftFrame,
            text=f"Position Search Status: {self.positions_search_status_message}",
            fg_color="transparent",
        ).grid(row=8, column=0, columnspan=2)

        # Accounts Frame Right Section
        self.StockerAccountsRightFrame = ctk.CTkFrame(
            master=self, width=710, fg_color="transparent"
        )
        self.StockerAccountsRightFrame.pack_propagate(False)
        self.StockerAccountsRightFrame.pack(
            side="right", fill="y", padx=(7.5, 15), pady=(5, 15)
        )

        # <-------------------------- SELECETED ACCOUNT INFORMATION HEADER -------------------------->

        self.selected_account_information_header = ctk.CTkFrame(
            master=self.StockerAccountsRightFrame, height=75, fg_color="transparent"
        )
        self.selected_account_information_header.pack_propagate(False)
        self.selected_account_information_header.pack(fill="x")
        self.selected_account_information_header.grid_propagate(False)

        self.selected_account_information_header.rowconfigure(0, weight=1)
        self.selected_account_information_header.rowconfigure(1, weight=1)
        self.selected_account_information_header.columnconfigure(0, weight=1)
        self.selected_account_information_header.columnconfigure(1, weight=1)
        self.selected_account_information_header.columnconfigure(2, weight=1)

        # SELECETED ACCOUNT INFORMATION HEADER | SELECTED ACCOUNT LABEL: "Selected Account: ..."
        self.selected_account_name = "Roth IRA"
        self.selected_account_label = ctk.CTkLabel(
            self.selected_account_information_header,
            text=f"Selected Account(s): {self.selected_account_name}",
            fg_color="transparent",
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=15,
        )

        # SELECETED ACCOUNT INFORMATION HEADER | SELECTED ACCOUNT TOTAL VALUE LABEL: "Total Value: ..."
        self.selected_account_total_value = 1500.0
        self.selected_account_total_value_label = ctk.CTkLabel(
            self.selected_account_information_header,
            text=f"Total Value: ${self.selected_account_total_value}",
            fg_color="transparent",
        ).grid(row=1, column=0, padx=15, sticky="w")

        # SELECETED ACCOUNT INFORMATION HEADER | SELECTED ACCOUNT CASH RESERVE LABEL: "Cash Reserve"
        self.selected_account_cash = 500.00
        self.selected_account_cash_label = ctk.CTkLabel(
            self.selected_account_information_header,
            text=f"Cash Reserve: ${self.selected_account_cash}",
            fg_color="transparent",
        ).grid(row=0, column=1)

        # SELECETED ACCOUNT INFORMATION HEADER | SELECTED ACCOUNT UPDATE CASH BUTTON: "Update Cash"
        self.selected_account_update_cash_button = ctk.CTkButton(
            self.selected_account_information_header, text=f"Update Cash"
        ).grid(row=1, column=1)

        # SELECETED ACCOUNT INFORMATION HEADER | SELECTED ACCOUNT STOCK ASSET VALUE LABEL: "Stock Asset Value: ..."
        self.selected_account_stock_asset_value = 1000.0
        self.selected_account_stock_asset_value_label = ctk.CTkLabel(
            self.selected_account_information_header,
            text=f"Stock Asset Value: ${self.selected_account_stock_asset_value}",
            fg_color="transparent",
        ).grid(row=0, column=2)

        # SELECETED ACCOUNT INFORMATION HEADER | SELECTED ACCOUNT STOCK ASSET VALUE BUTTON: "Refresh Value"
        self.selected_account_refresh_value_button = ctk.CTkButton(
            self.selected_account_information_header, text=f"Refresh Value"
        ).grid(row=1, column=2)

        # <-------------------------- SELECETED ACCOUNT INFORMATION TABLE -------------------------->

        self.selected_account_information_table_frame = ctk.CTkFrame(
            master=self.StockerAccountsRightFrame, fg_color="transparent"
        )
        self.selected_account_information_table_frame.pack_propagate(False)
        self.selected_account_information_table_frame.pack(fill="both", expand=True)
        self.selected_account_information_table_frame.grid_propagate(False)

        # SELECETED ACCOUNT INFORMATION TABLE | SELECETED ACCOUNT INFORMATION TABLE
        self.headers = [
            "ticker",
            "share count",
            "average cost",
            "current price",
            "asset value",
            "unrealized gain",
            "parent account",
        ]

        self.table_data = [
            self.headers,
            ["AAPL", 5, 200.00, 200.00, 1000.00, 0.0, "Roth IRA (Fidelity)"],
            ["AAPL", 5, 200.00, 200.00, 1000.00, 0.0, "Roth IRA (Fidelity)"],
            ["AAPL", 5, 200.00, 200.00, 1000.00, 0.0, "Roth IRA (Fidelity)"],
            ["AAPL", 5, 200.00, 200.00, 1000.00, 0.0, "Roth IRA (Fidelity)"],
            ["AAPL", 5, 200.00, 200.00, 1000.00, 0.0, "Roth IRA (Fidelity)"],
            ["AAPL", 5, 200.00, 200.00, 1000.00, 0.0, "Roth IRA (Fidelity)"],
            ["AAPL", 5, 200.00, 200.00, 1000.00, 0.0, "Roth IRA (Fidelity)"],
            ["AAPL", 5, 200.00, 200.00, 1000.00, 0.0, "Roth IRA (Fidelity)"],
            ["AAPL", 5, 200.00, 200.00, 1000.00, 0.0, "Roth IRA (Fidelity)"],
            ["AAPL", 5, 200.00, 200.00, 1000.00, 0.0, "Roth IRA (Fidelity)"],
        ]

        self.account_information_table = CTkTable(
            master=self.selected_account_information_table_frame,
            row=len(self.table_data),
            column=len(self.table_data[0]),
            values=self.table_data,
            header_color="grey",
            corner_radius=4,
            wraplength=75,
        )
        self.account_information_table.pack(pady=(15))
