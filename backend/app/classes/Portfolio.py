from .Account import Account

class Portfolio:

    def __init__(self, name: str):

        self.name = name
        self.accounts: dict[str, Account] = {}
        self._total_value = 0.0
        self._unrealized_gain = 0.0

    def add_account(self, account: Account) -> None:
        account._parent_portfolio = self
        self.accounts[account.name] = account
        self._total_value += account.total_value
        self._unrealized_gain += account.unrealized_gain
        print(f"{account.name.title()} held with {account.institution.title()} added to {self.name.title()} Portfolio successfully.")

    def delete_account(self, account: Account, account_name: str):
        if account:
            rem = self.accounts.pop(account.name, None)
        elif account_name:
            rem = self.accounts.pop(account_name.lower(), None)
        else:
            raise ValueError("AccountError: Must provide a Position or ticker.")    
        
        if rem is None:
                raise KeyError("PortfolioError: Account name not found, removal failed.")   
        self._total_value -= rem.total_value
        self._unrealized_gain -= rem.unrealized_gain
        print(f"{rem.name.upper()} held with {rem.institution.title()} was removed from {self.name.title()} Portfolio successfully.")
    

    @property
    def total_value(self):
        return self._total_value
    
    @property
    def unrealized_gain(self):
        return self._unrealized_gain
    
