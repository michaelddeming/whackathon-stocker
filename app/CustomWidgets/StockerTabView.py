
import customtkinter as ctk

class StockerTabView(ctk.CTkTabview):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.pack_propagate(False)

        self.add("Portfolio")
        self.add("Accounts")
        self.add("Transactions")
        self.add("Settings")

