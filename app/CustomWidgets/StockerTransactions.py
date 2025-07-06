import customtkinter as ctk

from CTkTable import *

class StockerTransactions(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, )

        # <-------------------------- SELECETED ACCOUNT INFORMATION TABLE -------------------------->

        self.transactions_scroll_frame = ctk.CTkScrollableFrame(
            master=self, fg_color="transparent"
        )
        self.transactions_scroll_frame.pack(fill="both", expand=True, pady=(15, 0))

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

        self.transactions_table = CTkTable(
            master=self.transactions_scroll_frame,
            row=len(self.table_data),
            column=len(self.table_data[0]),
            values=self.table_data,
            header_color="grey",
            corner_radius=4,
            wraplength=75,
        )
        self.transactions_table.pack(pady=15)


