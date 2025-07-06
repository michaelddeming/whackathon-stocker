
import customtkinter as ctk

class StockerAccounts(ctk.CTkFrame):
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.pack_propagate(False)

        # Accounts Frame Left Section
        self.StockerAccountsLeftFrame = ctk.CTkFrame(master=self, width=400, border_color="black", border_width=1)
        self.StockerAccountsLeftFrame.pack_propagate(False)
        self.StockerAccountsLeftFrame.grid_propagate(False)
        self.StockerAccountsLeftFrame.pack(side="left", fill="y", padx=(15, 7.5), pady=(5, 15))

        self.StockerAccountsLeftFrame.columnconfigure(0, weight=1)
        self.StockerAccountsLeftFrame.columnconfigure(1, weight=1)

        self.StockerAccountsLeftFrame.rowconfigure(0, weight=1) # Accounts Title
        self.StockerAccountsLeftFrame.rowconfigure(1, weight=1) # View Account(s) Label + Accounts Drop Down
        self.StockerAccountsLeftFrame.rowconfigure(2, weight=1) # View Account(s) Submit Button
        self.StockerAccountsLeftFrame.rowconfigure(3, weight=1) # View Account(s) Submit Status Label
        self.StockerAccountsLeftFrame.rowconfigure(4, weight=1) # Blank Space
        self.StockerAccountsLeftFrame.rowconfigure(5, weight=1) # Positions Title
        self.StockerAccountsLeftFrame.rowconfigure(6, weight=1) # Search Position(s) Label + Textbox
        self.StockerAccountsLeftFrame.rowconfigure(7, weight=1) # Search Positions Submit Button
        self.StockerAccountsLeftFrame.rowconfigure(8, weight=1) # Search Positions Submit Status Label


        
        
        # <-------------------------- ACCOUNT SELECT DROPDOWN MENU -------------------------->

        # TITLE: "Accounts"
        self.accounts_left_frame_title_label = ctk.CTkLabel(self.StockerAccountsLeftFrame, text=f"Accounts", fg_color="transparent").grid(row=0,column=0, columnspan=2)

        # ACCOUNT SELECT DROPDOWN | DROPDOWN LABEL: "Select Account(s)"
        self.select_accounts_dropdown_dropdown_label = ctk.CTkLabel(self.StockerAccountsLeftFrame, text=f"Select Account(s)", fg_color="transparent").grid(row=1,column=0)
        
        # ACCOUNT SELECT DROPDOWN | DROPDOWN-BOX: Account Names
        self.account_names = ["Roth IRA", "Taxable Account", "Traditional 401k"]
        self.select_accounts_dropdown_dropdown = ctk.CTkComboBox(master=self.StockerAccountsLeftFrame, values=self.account_names).grid(row=1,column=1)

        # ACCOUNT SELECT DROPDOWN | SUBMIT BUTTON: "View Account(s)"
        self.submit_account_view_button = ctk.CTkButton(master=self.StockerAccountsLeftFrame, text="View Account(s)").grid(row=2,column=0,columnspan=2)

        # ACCOUNT SELECT DROPDOWN | STATUS LABEL: "Select Account(s)"
        self.account_dropdown_status_message = "N/A"
        self.select_accounts_dropdown_status_label = ctk.CTkLabel(self.StockerAccountsLeftFrame, text=f"Status: {self.account_dropdown_status_message}", fg_color="transparent").grid(row=3,column=0,columnspan=2)
        
        
        # <-------------------------- POSITION SEARCH MENU -------------------------->

        # POSITION SEARCH MENU | TITLE: "Positions"
        self.positions_search_menu_title_label = ctk.CTkLabel(self.StockerAccountsLeftFrame, text=f"Positions", fg_color="transparent").grid(row=5,column=0, columnspan=2)

        # POSITION SEARCH MENU | POSITION SEARCHBOX LABEL: "Search Position(s)"
        self.positions_search_searchbox_label = ctk.CTkLabel(self.StockerAccountsLeftFrame, text=f"Search Position(s)", fg_color="transparent").grid(row=6,column=0)
        
        # POSITION SEARCH MENU | POSITION SEARCHBOX: "Ticker"
        self.positions_search_searchbox = ctk.CTkEntry(master=self.StockerAccountsLeftFrame, placeholder_text="Ticker (AAPL)" ).grid(row=6,column=1)

        # POSITION SEARCH MENU | POSITION SEARCH SUBMIT BUTTON: "Search Position(s)"
        self.positions_search_submit_button = ctk.CTkButton(master=self.StockerAccountsLeftFrame, text="Search Position(s)").grid(row=7,column=0,columnspan=2)

        # POSITION SEARCH MENU | POSITION SEARCH SUBMIT STATUS LABEL: "Status: ..."
        self.positions_search_status_message = "N/A"
        self.position_search_status_label = ctk.CTkLabel(self.StockerAccountsLeftFrame, text=f"Position Search Status: {self.positions_search_status_message}", fg_color="transparent").grid(row=8,column=0,columnspan=2)
    

        
        # Accounts Frame Right Section
        self.StockerAccountsRightFrame = ctk.CTkFrame(master=self, width=710, border_color="black", border_width=1)

        self.StockerAccountsRightFrame.pack(side="right", fill="y", padx=(7.5, 15), pady=(5, 15))