
from datetime import datetime

class Transaction:

    def __init__(self,
                 transaction_type: str,
                 amount: float,
                 parent: object,
                 notes: str=None):
        
        self.transaction_types = {"add_position", 
                                  "delete_position", 
                                  "overwrite_cash", 
                                  "add_cash", 
                                  "delete_cash",
                                  "add_account",
                                  "delete_account",
                                  "update_position"
                                  }
        if transaction_type not in self.transaction_types:
            raise ValueError("TransactionError: Invalid transaction_type.")
        self.transaction_type = transaction_type
        self.amount = amount
        self.notes = notes
        self.parent = parent
        self.datetime = datetime.today()
        

    def to_dict(self):
        
        transaction_dict = {
            "transaction_type": self.transaction_type,
            "amount": self.amount,
            "datetime": self.datetime.isoformat(),
            "parent": self.parent.name,
            "notes": "N/A" if self.notes is None else self.notes,
        }

        return transaction_dict



    @property
    def description(self):
        return f"Transaction: {self.parent.name.title()} | {self.transaction_type} | {self.amount} on {self.datetime.date}@{self.datetime.time} | NOTES: {"N/A" if self.notes is None else self.notes.capitalize()}."