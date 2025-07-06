import customtkinter as ctk
from CTkTable import *


class StockerAccounts(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.pack_propagate(False)

        # Accounts Frame Left Section
        self.StockerAccountsLeftFrame = ctk.CTkFrame(
            master=self, width=300, fg_color="transparent"
        )
        self.StockerAccountsLeftFrame.pack_propagate(False)
        self.StockerAccountsLeftFrame.grid_propagate(False)
        self.StockerAccountsLeftFrame.pack(
            side="left", fill="y", padx=(15, 7.5), pady=(5, 15)
        )

        # <-------------------------- ACCOUNT SELECT DROPDOWN MENU -------------------------->
        self.account_select_frame = ctk.CTkFrame(
            master=self.StockerAccountsLeftFrame,
        )
        self.account_select_frame.pack(side="top", fill="x", pady=(75,0))
        self.account_select_frame.grid_propagate(False)
        self.account_select_frame.rowconfigure(0, weight=1)
        self.account_select_frame.rowconfigure(1, weight=1)
        self.account_select_frame.rowconfigure(2, weight=1)
        self.account_select_frame.rowconfigure(3, weight=1)

        self.account_select_frame.columnconfigure(0, weight=1)
        self.account_select_frame.columnconfigure(1, weight=1)

        # TITLE: "Accounts"
        self.accounts_left_frame_title_label = ctk.CTkLabel(
            self.account_select_frame, text=f"Accounts", fg_color="transparent"
        ).grid(row=0, column=0, columnspan=2)

        # ACCOUNT SELECT DROPDOWN | DROPDOWN LABEL: "Select Account(s)"
        self.select_accounts_dropdown_dropdown_label = ctk.CTkLabel(
            self.account_select_frame,
            text=f"Select Account(s)",
            fg_color="transparent",
        ).grid(row=1, column=0)

        # ACCOUNT SELECT DROPDOWN | DROPDOWN-BOX: Account Names
        self.account_names = ["Roth IRA", "Taxable Account", "Traditional 401k", "all"]
        self.select_accounts_dropdown_dropdown = ctk.CTkComboBox(
            master=self.account_select_frame, values=self.account_names
        ).grid(row=1, column=1)

        # ACCOUNT SELECT DROPDOWN | SUBMIT BUTTON: "View Account(s)"
        self.submit_account_view_button = ctk.CTkButton(
            master=self.account_select_frame, text="View Account(s)"
        ).grid(row=2, column=0, columnspan=2)

        # ACCOUNT SELECT DROPDOWN | STATUS LABEL: "Select Account(s)"
        self.account_dropdown_status_message = "N/A"
        self.select_accounts_dropdown_status_label = ctk.CTkLabel(
            self.account_select_frame,
            text=f"Status: {self.account_dropdown_status_message}",
            fg_color="transparent",
        ).grid(row=3, column=0, columnspan=2)

        # <-------------------------- POSITION SEARCH MENU -------------------------->
        self.position_search_frame = ctk.CTkFrame(
            master=self.StockerAccountsLeftFrame,
        )
        self.position_search_frame.pack(side="bottom", fill="x", pady=(0,75))
        self.position_search_frame.grid_propagate(False)
        self.position_search_frame.rowconfigure(0, weight=1)
        self.position_search_frame.rowconfigure(1, weight=1)
        self.position_search_frame.rowconfigure(2, weight=1)
        self.position_search_frame.rowconfigure(3, weight=1)
        self.position_search_frame.rowconfigure(3, weight=1)

        self.position_search_frame.columnconfigure(0, weight=1)
        self.position_search_frame.columnconfigure(1, weight=1)
        # POSITION SEARCH MENU | TITLE: "Positions"
        self.positions_search_menu_title_label = ctk.CTkLabel(
            self.position_search_frame, text=f"Positions", fg_color="transparent"
        ).grid(row=0, column=0, columnspan=2)

        # POSITION SEACH MENU | POSITION HEADING/FILTER DROPDOWN LABEL: "Position Filter:"
        self.position_filter_dropdown_label = ctk.CTkLabel(
            self.position_search_frame, text=f"Position Filter", fg_color="transparent"
        ).grid(row=1, column=0)

        # POSITION SEARCH MENU | POSITION HEADING/FILTER DROPDOWN-BOX: "Position Heading"
        self.position_headings = [
            "ticker",
            "share count",
            "average cost",
            "current price",
            "asset value",
            "unrealized gain",
            "parent account",
        ]
        self.position_search_heading_dropdown = ctk.CTkComboBox(
            master=self.position_search_frame, values=self.position_headings
        ).grid(row=1, column=1)

        # POSITION SEARCH MENU | POSITION SEARCHBOX LABEL: "Search Position(s)"
        self.positions_search_searchbox_label = ctk.CTkLabel(
            self.position_search_frame,
            text=f"Search Position(s)",
            fg_color="transparent",
        ).grid(row=2, column=0)

        # POSITION SEARCH MENU | POSITION SEARCHBOX: "Ticker"
        self.positions_search_searchbox = ctk.CTkEntry(
            master=self.position_search_frame, placeholder_text="Type Here"
        ).grid(row=2, column=1)

        # POSITION SEARCH MENU | POSITION SEARCH SUBMIT BUTTON: "Search Position(s)"
        self.positions_search_submit_button = ctk.CTkButton(
            master=self.position_search_frame, text="Search Position(s)"
        ).grid(row=3, column=0, columnspan=2)

        # POSITION SEARCH MENU | POSITION SEARCH SUBMIT STATUS LABEL: "Status: ..."
        self.positions_search_status_message = "N/A"
        self.position_search_status_label = ctk.CTkLabel(
            self.position_search_frame,
            text=f"Position Search Status: {self.positions_search_status_message}",
            fg_color="transparent",
        ).grid(row=4, column=0, columnspan=2)

        # <-------------------------- SELECETED ACCOUNT INFORMATION HEADER -------------------------->

        # Accounts Frame Right Section
        self.StockerAccountsRightFrame = ctk.CTkFrame(
            master=self, fg_color="transparent",
        )
        self.StockerAccountsRightFrame.pack_propagate(False)
        self.StockerAccountsRightFrame.pack(
            side="right", fill="both", expand=True, padx=(7.5, 15), pady=(5, 15)
        )
        self.selected_account_information_header = ctk.CTkFrame(
            master=self.StockerAccountsRightFrame, height=75, fg_color="transparent"
        )
        self.selected_account_information_header.pack_propagate(False)
        self.selected_account_information_header.pack(fill="x", pady=(15, 0))
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

        self.selected_account_information_table_frame = ctk.CTkScrollableFrame(
            master=self.StockerAccountsRightFrame, fg_color="transparent"
        )
        self.selected_account_information_table_frame.pack(fill="both", expand=True, pady=(15, 0))

        # SELECETED ACCOUNT INFORMATION TABLE | SELECETED ACCOUNT INFORMATION TABLE

        self.table_data = [
            self.position_headings,
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
