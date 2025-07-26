import customtkinter as ctk
from Classes.Position import Position
from Classes.Account import Account

class StockerAddPositionPopUp(ctk.CTkToplevel):
    def __init__(self, account: Account, positions_table, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.attributes("-topmost", True)
        self.account = account
        self.positions_table = positions_table
        
        for i in range(5):
            self.rowconfigure(i, weight=1)
        
        for i in range(2):
            self.columnconfigure(i, weight=1)

        self.add_position_label = ctk.CTkLabel(self, text="Add Position")
        self.add_position_label.grid(row=0, column=0, columnspan=2)
        # ----------------------------------------------------------
        self.ticker_label = ctk.CTkLabel(self, text="Ticker:")
        self.ticker_label.grid(row=1, column=0, sticky="E", padx=5)
        self.ticker_entry = ctk.CTkEntry(self, placeholder_text="AAPL")
        self.ticker_entry.grid(row=1, column=1, sticky="W", padx=5)
        # ----------------------------------------------------------
        self.share_count_label = ctk.CTkLabel(self, text="Share Count:")
        self.share_count_label.grid(row=2, column=0, sticky="E", padx=5)
        self.share_count_entry = ctk.CTkEntry(self, placeholder_text="2 or 2.35")
        self.share_count_entry.grid(row=2, column=1, sticky="W", padx=5)
        # ----------------------------------------------------------
        self.average_cost_label = ctk.CTkLabel(self, text="Average Cost:")
        self.average_cost_label.grid(row=3, column=0, sticky="E", padx=5)
        self.average_cost_entry = ctk.CTkEntry(self, placeholder_text="2 or 2.35")
        self.average_cost_entry.grid(row=3, column=1, sticky="W", padx=5)
        # ----------------------------------------------------------
        self.add_position_button = ctk.CTkButton(self, text="Add Position", command=self.add_position)
        self.add_position_button.grid(row=4, column=0, columnspan=2)
    
    def add_position(self):

        # get the ticker info from user input
        ticker = self.ticker_entry.get()
        if ticker == "":
            print("Error Blank Ticker")
            return 
        ticker = ticker.lower().strip()

        # get the share_count from user_input
        share_count = self.share_count_entry.get()
        if share_count == "":
            print("Error Blank share_count")
            return 
        try:
            share_count = float(share_count.strip())
        except ValueError:
            print("Error on share_count integer conversion.")
            return
        
        # get the average_cost from user_input
        average_cost = self.average_cost_entry.get()
        if average_cost == "":
            print("Error Blank average_cost")
            return 
        try:
            average_cost = float(average_cost.strip())
        except ValueError:
            print("Error on average_cost integer conversion.")
            return
        
        new_position = Position(ticker=ticker, shares=share_count, average_cost=average_cost)
        self.account.add_positions(new_position)
        self.positions_table.add_row([new_position.ticker, new_position.shares, new_position.average_cost, new_position.current_price, new_position.total_value, new_position.unrealized_gain, new_position.parent_account.name])
        self.master.populate_account_info_heading(account_name_keyword=self.account.name)
        






