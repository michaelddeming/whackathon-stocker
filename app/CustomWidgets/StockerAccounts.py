
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

        self.StockerAccountsLeftFrame.rowconfigure(0, weight=1) # Title
        self.StockerAccountsLeftFrame.rowconfigure(1, weight=1) # Blank Space
        self.StockerAccountsLeftFrame.rowconfigure(2, weight=1) # View Account(s) Label + Accounts Drop Down


        ctk.CTkLabel(self.StockerAccountsLeftFrame, text=f"Accounts + Positions", fg_color="transparent").grid(row=0,column=0, columnspan=2)

        

        
        # Accounts Frame Right Section
        self.StockerAccountsRightFrame = ctk.CTkFrame(master=self, width=710, border_color="black", border_width=1)

        self.StockerAccountsRightFrame.pack(side="right", fill="y", padx=(7.5, 15), pady=(5, 15))