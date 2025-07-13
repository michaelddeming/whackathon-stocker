import customtkinter as ctk
from CTkTable import *


class StockerAccounts(ctk.CTkFrame):

    def __init__(self, master, portfolio, **kwargs):
        super().__init__(master, **kwargs)
        self.PORTFOLIO = portfolio
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
        )
        self.select_accounts_dropdown_dropdown_label.grid(row=1, column=0)

        # ACCOUNT SELECT DROPDOWN | DROPDOWN-BOX: Account Names
        self.account_names = ["All Accounts"] + [key.title() for key in self.PORTFOLIO.accounts.keys()]
        print(self.account_names)
        self.select_accounts_dropdown_dropdown = ctk.CTkComboBox(
            master=self.account_select_frame, values=self.account_names
        )
        self.select_accounts_dropdown_dropdown.grid(row=1, column=1)

        # ACCOUNT SELECT DROPDOWN | SUBMIT BUTTON: "View Account(s)"
        self.submit_account_view_button = ctk.CTkButton(
            master=self.account_select_frame, text="View Account(s)", command=self.view_accounts
        )
        self.submit_account_view_button.grid(row=2, column=0, columnspan=2)

        # ACCOUNT SELECT DROPDOWN | STATUS LABEL: "Select Account(s)"
        self.select_accounts_dropdown_status_label = ctk.CTkLabel(
            self.account_select_frame,
            text=f"Status: N/A",
            fg_color="transparent",
        )
        self.select_accounts_dropdown_status_label.grid(row=3, column=0, columnspan=2)

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
        )
        self.positions_search_menu_title_label.grid(row=0, column=0, columnspan=2)

        # POSITION SEACH MENU | POSITION HEADING/FILTER DROPDOWN LABEL: "Position Filter:"
        self.position_filter_dropdown_label = ctk.CTkLabel(
            self.position_search_frame, text=f"Position Filter", fg_color="transparent"
        )
        self.position_filter_dropdown_label.grid(row=1, column=0)

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
        )
        self.position_search_heading_dropdown.grid(row=1, column=1)

        # POSITION SEARCH MENU | POSITION SEARCHBOX LABEL: "Search Position(s)"
        self.positions_search_searchbox_label = ctk.CTkLabel(
            self.position_search_frame,
            text=f"Search Position(s)",
            fg_color="transparent",
        )
        self.positions_search_searchbox_label.grid(row=2, column=0)

        # POSITION SEARCH MENU | POSITION SEARCHBOX: "Ticker"
        self.positions_search_searchbox = ctk.CTkEntry(
            master=self.position_search_frame, placeholder_text="Type Here"
        )
        self.positions_search_searchbox.grid(row=2, column=1)

        # POSITION SEARCH MENU | POSITION SEARCH SUBMIT BUTTON: "Search Position(s)"
        self.positions_search_submit_button = ctk.CTkButton(
            master=self.position_search_frame, text="Search Position(s)", command=self.search_positions
        )
        self.positions_search_submit_button.grid(row=3, column=0)

        # POSITION SEARCH MENU | POSITION SEARCH RESET BUTTON: "Reset Position(s)"
        self.positions_search_reset_button = ctk.CTkButton(
            master=self.position_search_frame, text="Reset Position(s)", command=self.reset_positions
        )
        self.positions_search_reset_button.grid(row=3, column=1)

        # POSITION SEARCH MENU | POSITION SEARCH SUBMIT STATUS LABEL: "Status: ..."
        self.positions_search_status_message = "N/A"
        self.position_search_status_label = ctk.CTkLabel(
            self.position_search_frame,
            text=f"Status: {self.positions_search_status_message}",
            fg_color="transparent",
        )
        self.position_search_status_label.grid(row=4, column=0, columnspan=2)

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
        self.selected_account_name = "All Accounts"
        self.selected_account_label = ctk.CTkLabel(
            self.selected_account_information_header,
            text=f"Selected Account(s): {self.selected_account_name}",
            fg_color="transparent",
        )
        self.selected_account_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=15,
        )

        # SELECETED ACCOUNT INFORMATION HEADER | SELECTED ACCOUNT TOTAL VALUE LABEL: "Total Value: ..."
        self.selected_account_total_value = self.PORTFOLIO.total_value
        self.selected_account_total_value_label = ctk.CTkLabel(
            self.selected_account_information_header,
            text=f"Total Value: ${self.selected_account_total_value}",
            fg_color="transparent",
        )
        self.selected_account_total_value_label.grid(row=1, column=0, padx=15, sticky="w")

        # SELECETED ACCOUNT INFORMATION HEADER | SELECTED ACCOUNT CASH RESERVE LABEL: "Cash Reserve"
        self.selected_account_cash = self.PORTFOLIO.cash
        self.selected_account_cash_label = ctk.CTkLabel(
            self.selected_account_information_header,
            text=f"Cash Reserve: ${self.selected_account_cash}",
            fg_color="transparent",
        )
        self.selected_account_cash_label.grid(row=0, column=1)

        # SELECETED ACCOUNT INFORMATION HEADER | SELECTED ACCOUNT UPDATE CASH BUTTON: "Update Cash"
        self.selected_account_update_cash_button = ctk.CTkButton(
            self.selected_account_information_header, text=f"Update Cash"
        )
        self.selected_account_update_cash_button.grid(row=1, column=1)

        # SELECETED ACCOUNT INFORMATION HEADER | SELECTED ACCOUNT STOCK ASSET VALUE LABEL: "Stock Asset Value: ..."
        self.selected_account_stock_asset_value = self.PORTFOLIO.stock_asset_value
        self.selected_account_stock_asset_value_label = ctk.CTkLabel(
            self.selected_account_information_header,
            text=f"Stock Asset Value: ${self.selected_account_stock_asset_value}",
            fg_color="transparent",
        )
        self.selected_account_stock_asset_value_label.grid(row=0, column=2)

        # SELECETED ACCOUNT INFORMATION HEADER | SELECTED ACCOUNT STOCK ASSET VALUE BUTTON: "Refresh Value"
        self.selected_account_refresh_value_button = ctk.CTkButton(
            self.selected_account_information_header, text=f"Refresh Value", command=self.refresh_account_view
        )
        self.selected_account_refresh_value_button.grid(row=1, column=2)

        # <-------------------------- SELECETED ACCOUNT INFORMATION TABLE -------------------------->

        self.selected_account_information_table_frame = ctk.CTkScrollableFrame(
            master=self.StockerAccountsRightFrame, fg_color="transparent"
        )
        self.selected_account_information_table_frame.pack(fill="both", expand=True, pady=(15, 0))

        # SELECETED ACCOUNT INFORMATION TABLE | SELECETED ACCOUNT INFORMATION TABLE
    
        self.table_data = self.populate_position_matrix("all accounts")
            
        

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


    def populate_position_matrix(self, account_name_keyword: str) -> list:
        # "ticker",
        # "share count",
        # "average cost",
        # "current price",
        # "asset value",
        # "unrealized gain",
        # "parent account",
        data = {}

        for account in self.PORTFOLIO.accounts.values():
            account_data = []
            account_positions = account.positions.values()
            for position in account_positions:
                account_data.append([position.ticker, position.shares, position.average_cost, position.current_price, position.total_value, position.unrealized_gain, position.parent_account.name])
                
            data[account.name] = account_data

        account_positions = [self.position_headings]
        
        account_name_keyword = account_name_keyword.lower()
        match account_name_keyword:
            
            case "all accounts":

                for account in data.values():
                    account_positions += account
            
            case _:
                account_positions += data.get(account_name_keyword, None)
        
        # populate the positions matrix on the accounts page
        return account_positions
        

    def populate_account_info_heading(self, account_name_keyword: str):
        account_name_keyword = account_name_keyword.lower()
        match account_name_keyword:

            case "all accounts":
                self.selected_account_label.configure(text=f"Selected Account(s): All Accounts")
                self.selected_account_total_value_label.configure(text=f"Total Value: ${self.PORTFOLIO.total_value}")
                self.selected_account_cash_label.configure(text=f"Cash Reserve: ${self.PORTFOLIO.cash}")
                self.selected_account_stock_asset_value_label.configure(text=f"Stock Asset Value: ${self.PORTFOLIO.stock_asset_value}")
            case _:
                selected_account = self.PORTFOLIO.accounts.get(account_name_keyword, None)
                if selected_account is None:
                    raise ValueError(f"AccountHeadingError: {account_name_keyword} not found in {self.PORTFOLIO.name.title()}.")
                self.selected_account_label.configure(text=f"Selected Account(s): {selected_account.name.title()}")
                self.selected_account_total_value_label.configure(text=f"Total Value: ${selected_account.total_value}")
                self.selected_account_cash_label.configure(text=f"Cash Reserve: ${selected_account.cash}")
                self.selected_account_stock_asset_value_label.configure(text=f"Stock Asset Value: ${selected_account.stock_asset_value}")

    def view_accounts(self):

        account_name = self.select_accounts_dropdown_dropdown.get()

        if account_name is None:
            print("Account name is None.")
            return
        account_name = account_name.lower()

        updated_position_matrix = self.populate_position_matrix(account_name_keyword=account_name)
        self.table_data = updated_position_matrix
        self.account_information_table.configure(values=updated_position_matrix, rows=len(updated_position_matrix), columns=len(self.position_headings))
        if len(updated_position_matrix) > 1:
            self.update_account_status_label(status_message=f"{len(updated_position_matrix) - 1} Position(s) found!\nAccount View updated.")
        else:
            self.update_account_status_label(status_message=f"No Positions found!\nAccount View not updated.")

        self.populate_account_info_heading(account_name_keyword=account_name)


    def update_account_status_label(self, status_message: str):
        self.select_accounts_dropdown_status_label.configure(text=f"Status: {status_message}")

    def refresh_account_view(self):
        self.PORTFOLIO.refresh_portfolio()
        self.view_accounts()
        
    def search_positions(self):

        # get the filter and user search input

        search_filter = self.position_search_heading_dropdown.get()
        user_input = self.positions_search_searchbox.get().strip()

        if search_filter not in self.position_headings:
            self.update_search_positions_status_label(status_message=f"Invalid search filter!\nSelect filter option from dropdown.")
            return

        if user_input == "" or user_input == None:
            self.update_search_positions_status_label(status_message=f"Invalid search input!\nSearch input can't be blank.")
            return

        filtered_positions = [self.position_headings]

        match search_filter:

            case "ticker":
                user_input = user_input.lower()
                index = self.position_headings.index("ticker")
                filtered_positions.extend(position for position in self.table_data[1:] if position[index].lower() == user_input)

                
            case "share count":
                filtered_positions.extend(self.position_filter_search_float_helper(user_input=user_input, heading_filter="share count"))

            case "average cost":
                filtered_positions.extend(self.position_filter_search_float_helper(user_input=user_input, heading_filter="average cost"))

            case "current price":
                filtered_positions.extend(self.position_filter_search_float_helper(user_input=user_input, heading_filter="current price"))

            case "asset value":
                filtered_positions.extend(self.position_filter_search_float_helper(user_input=user_input, heading_filter="asset value"))

            case "unrealized gain":
                filtered_positions.extend(self.position_filter_search_float_helper(user_input=user_input, heading_filter="unrealized gain"))

            case "parent account":
                user_input = user_input.lower()
                index = self.position_headings.index("parent account")
                filtered_positions.extend(position for position in self.table_data[1:] if position[index].lower() == user_input)
                print(filtered_positions)

        
        if len(filtered_positions) > 1:
            self.account_information_table.configure(values=filtered_positions, rows=len(filtered_positions), columns=len(self.position_headings))
            self.update_search_positions_status_label(status_message=f"{len(filtered_positions) - 1} Position(s) found!\nPosition View updated.")
    
        else:
            self.update_search_positions_status_label(status_message=f"No Positions found!\nPosition View not updated.")
            return 

 

    def update_search_positions_status_label(self, status_message: str) -> None:
        self.position_search_status_label.configure(text=f"Status: {status_message}")

    def position_filter_search_float_helper(self, user_input: str, heading_filter: str) -> list:
        try:
            user_input = float(user_input)
        except ValueError:
            self.update_search_positions_status_label(status_message=f"Invalid search input !\nInput could not be converted to float.")
            return []
        try:
            index = self.position_headings.index(heading_filter)
        except ValueError:
            print("Invalid heading filter, heading not found.")
            return []
        return [position for position in self.table_data[1:] if position[index] >= user_input]

    def reset_positions(self):
        self.account_information_table.configure(values=self.table_data, rows=len(self.table_data), columns=len(self.position_headings))
        self.update_search_positions_status_label(status_message=f"Reset successful!\nPosition View reset.")
                


