from .Account import Account

class Portfolio:

    def __init__(self, name: str):

        self.name = name
        self.accounts: dict[str, Account] = {}
        self._cash = 0.0
        self._stock_asset_value = 0.0
        self._unrealized_gain = 0.0
        print(f"New Portfolio '{self.name}' successfully created.\n")

    def add_account(self, account: Account) -> None:
        # sync the account to the portfolio
        account._parent_portfolio = self

        # add the account to the accounts data struct
        self.accounts[account.name] = account

        # increase the Portfolio stock_asset_value, unrealized_gain, and cash proportionally
        self._stock_asset_value += account.stock_asset_value
        self._unrealized_gain += account.unrealized_gain
        self._cash += account.cash

        # print success message
        print(f"{account.name.title()} held with {account.institution.title()} added to {self.name.title()} Portfolio successfully.\n")

    def delete_account(self, account: Account, account_name: str):
        if account:
            rem = self.accounts.pop(account.name, None)
        elif account_name:
            rem = self.accounts.pop(account_name.lower(), None)
        else:
            raise ValueError("AccountError: Must provide a Position or ticker.")    
        
        if rem is None:
                raise KeyError("PortfolioError: Account name not found, removal failed.")  
        self._stock_asset_value -= rem.stock_asset_value
        self._unrealized_gain -= rem.unrealized_gain
        self._cash -= rem.cash    

        print(f"{rem.name.upper()} held with {rem.institution.title()} was removed from {self.name.title()} Portfolio successfully.")
    

    @property
    def total_value(self):
        return round(self._stock_asset_value + self._cash, 2)
    
    @property
    def unrealized_gain(self):
        return round(self._unrealized_gain, 2)
    
    @property
    def stock_asset_value(self):
        return round(self._stock_asset_value, 2)
    
    @property
    def cash(self):
        return round(self._cash, 2)