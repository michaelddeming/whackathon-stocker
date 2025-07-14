import customtkinter as ctk

class StockerAddPositionPopUp(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.attributes("-topmost", True)
        
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
        self.add_position_button = ctk.CTkButton(self, text="Add Position")
        self.add_position_button.grid(row=4, column=0, columnspan=2)



