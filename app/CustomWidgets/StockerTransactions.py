import customtkinter as ctk

from CTkTable import *

class StockerTransactions(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, )

        transactions_table = CTkTable(master=self,)


