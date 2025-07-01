from .Account import Account

class Portfolio:

    def __init__(self, name: str):

        self.name = name
        self.accounts: dict[str, Account] = {}

    def add_account(self, account: Account) -> None:
        self.accounts[account.name] = account
        print(f"{account.name.title()} held with {account.institution.title()} added to {self.name.title()} Portfolio successfully.")

    def delete_account(self, account: Account, account_name: str):
        if account:
            rem = self.accounts.pop(account.name, None)
            if rem is None:
                raise KeyError("PortfolioError: Account not found, removal failed.")
            else:
                print(f"{rem.name.upper()} held with {rem.institution.title()} was removed from {self.name.title()} Portfolio successfully.")
        elif account_name:
            rem = self.accounts.pop(account_name.lower(), None)
            if rem is None:
                raise KeyError("PortfolioError: Account name not found, removal failed.")
            else:
                print(f"{rem.name.upper()} held with {rem.institution.title()} was removed from {self.name.title()} Portfolio successfully.")
        else:
            raise ValueError("AccountError: Must provide a Position or ticker.")

    @property
    def total_value(self):

        if not self.accounts:
            return 0.0
        total_value = 0.0
        for account in self.accounts.values():
            total_value += account.total_value
        return total_value
    
    @property
    def unrealized_gain(self):
        if not self.accounts:
            return 0.0
        total_gain = 0.0
        for account in self.accounts.values():
            total_gain += account.unrealized_gain
        return total_gain
    
