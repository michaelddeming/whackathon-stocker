import customtkinter as ctk
from CustomWidgets.StockerPortfolio import StockerPortfolio
from CustomWidgets.StockerAccounts import StockerAccounts
from CustomWidgets.StockerTransactions import StockerTransactions


class StockerTabView(ctk.CTkTabview):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack_propagate(False)
        self.add("Portfolio")
        self.add("Accounts")
        self.add("Transactions")
        self.add("Settings")

        self.StockerPortfolio = StockerPortfolio(master=self.tab("Portfolio"))
        self.StockerPortfolio.pack(fill="both", expand=True)
        self.StockerAccounts = StockerAccounts(master=self.tab("Accounts"))
        self.StockerAccounts.pack(fill="both", expand=True)
        self.StockerTransactions = StockerTransactions(master=self.tab("Transactions"))
        self.StockerTransactions.pack(fill="both", expand=True)
