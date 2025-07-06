import customtkinter as ctk

from CTkTable import *

class StockerTransactions(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, )

        # Transactions Frame Left Section
        self.StockerTransactionsLeftFrame = ctk.CTkFrame(
            master=self, width=300, fg_color="transparent"
        )
        self.StockerTransactionsLeftFrame.pack_propagate(False)
        self.StockerTransactionsLeftFrame.grid_propagate(False)
        self.StockerTransactionsLeftFrame.pack(
            side="left", fill="y", padx=(15, 7.5), pady=(5, 15)
        )

# <-------------------------- TRANSACTION SEARCH MENU -------------------------->
        self.transaction_search_menu_frame = ctk.CTkFrame(
            master=self.StockerTransactionsLeftFrame,
        )
        self.transaction_search_menu_frame.pack(fill="x", expand=True)
        self.transaction_search_menu_frame.grid_propagate(False)
        self.transaction_search_menu_frame.rowconfigure(0, weight=1)
        self.transaction_search_menu_frame.rowconfigure(1, weight=1)
        self.transaction_search_menu_frame.rowconfigure(2, weight=1)
        self.transaction_search_menu_frame.rowconfigure(3, weight=1)
        self.transaction_search_menu_frame.rowconfigure(3, weight=1)

        self.transaction_search_menu_frame.columnconfigure(0, weight=1)
        self.transaction_search_menu_frame.columnconfigure(1, weight=1)
        # TRANSACTION SEARCH MENU | TITLE: "Transactions"
        self.transactions_search_menu_title_label = ctk.CTkLabel(
            self.transaction_search_menu_frame, text=f"Transactions", fg_color="transparent"
        ).grid(row=0, column=0, columnspan=2)

        # TRANSACTION SEACH MENU | TRANSACTION HEADING/FILTER DROPDOWN LABEL: "TRANSACTION Filter:"
        self.transaction_filter_dropdown_label = ctk.CTkLabel(
            self.transaction_search_menu_frame, text=f"Transactions Filter", fg_color="transparent"
        ).grid(row=1, column=0)

        # TRANSACTION SEARCH MENU | TRANSACTION HEADING/FILTER DROPDOWN-BOX: "Transaction Heading"
        self.transaction_headings = [
            "ticker",
            "share count",
            "average cost",
            "current price",
            "asset value",
            "unrealized gain",
            "parent account",
        ]
        self.transaction_search_heading_dropdown = ctk.CTkComboBox(
            master=self.transaction_search_menu_frame, values=self.transaction_headings
        ).grid(row=1, column=1)

        # TRANSACTION SEARCH MENU | TRANSACTION SEARCHBOX LABEL: "Search Transaction(s)"
        self.transactions_search_searchbox_label = ctk.CTkLabel(
            self.transaction_search_menu_frame,
            text=f"Search Transaction(s)",
            fg_color="transparent",
        ).grid(row=2, column=0)

        # TRANSACTION SEARCH MENU | TRANSACTION SEARCHBOX: "Ticker"
        self.transactions_search_searchbox = ctk.CTkEntry(
            master=self.transaction_search_menu_frame, placeholder_text="Type Here"
        ).grid(row=2, column=1)

        # TRANSACTION SEARCH MENU | TRANSACTION SEARCH SUBMIT BUTTON: "Search Transaction(s)"
        self.transactions_search_submit_button = ctk.CTkButton(
            master=self.transaction_search_menu_frame, text="Search Transaction(s)"
        ).grid(row=3, column=0, columnspan=2)

        # TRANSACTION SEARCH MENU | TRANSACTION SEARCH SUBMIT STATUS LABEL: "Status: ..."
        self.transactions_search_status_message = "N/A"
        self.transaction_search_status_label = ctk.CTkLabel(
            self.transaction_search_menu_frame,
            text=f"Transaction Search Status: {self.transactions_search_status_message}",
            fg_color="transparent",
        ).grid(row=4, column=0, columnspan=2)








         # Transactions Frame Right Section
        self.StockerTransactionsRightFrame = ctk.CTkFrame(
            master=self, fg_color="transparent",
        )
        self.StockerTransactionsRightFrame.pack_propagate(False)
        self.StockerTransactionsRightFrame.pack(
            side="right", fill="both", expand=True, padx=(7.5, 15), pady=(5, 15)
        )

        # <-------------------------- SELECETED TRANSACTION INFORMATION TABLE -------------------------->

        self.transactions_scroll_frame = ctk.CTkScrollableFrame(
            master=self.StockerTransactionsRightFrame, fg_color="transparent"
        )
        self.transactions_scroll_frame.pack(fill="both", expand=True, pady=(15, 0))

        # SELECETED TRANSACTION INFORMATION TABLE | SELECETED TRANSACTION INFORMATION TABLE

        self.table_data = [
            self.transaction_headings,
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
        self.transactions_table.pack()


