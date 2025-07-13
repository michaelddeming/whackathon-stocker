from .Account import Account
from .Position import Position
import json
from typing import Self


class Portfolio:

    defaults = {
        "name": "new portfolio",
        "accounts": {},
        "cash": 0.0,
        "stock_asset_value": 0.0,
        "unrealized_gain": 0.0,
    }

    def __init__(
        self,
        name: str | None = None,
        accounts: dict[str, Account] | None = None,
        cash: float | None = None,
        stock_asset_value: float | None = None,
        unrealized_gain: float | None = None,
    ):

        self.name = name.lower() if name is not None else self.defaults.get("name")
        self.accounts = (
            accounts  if accounts is not None else self.defaults.get("accounts")
        )
        self._cash = cash if cash is not None else self.defaults.get("cash")
        self._stock_asset_value = (
            stock_asset_value if stock_asset_value is not None else self.defaults.get("stock_asset_value")
        )
        self._unrealized_gain = (
            unrealized_gain if unrealized_gain is not None else self.defaults.get("unrealized_gain")
        )
        print(f"New Portfolio '{self.name}' successfully created.\n")

    def add_accounts(self, *accounts: list[Account]) -> None:
        for account in accounts:
            # sync the account to the portfolio
            account._parent_portfolio = self

            # add the account to the accounts data struct
            self.accounts[account.name] = account

            # increase the Portfolio stock_asset_value, unrealized_gain, and cash proportionally
            self._stock_asset_value += account.stock_asset_value
            self._unrealized_gain += account.unrealized_gain
            self._cash += account.cash

            # print success message
            print(
                f"{account.name.title()} held with {account.institution.title()} added to {self.name.title()} Portfolio successfully.\n"
            )

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

        print(
            f"{rem.name.upper()} held with {rem.institution.title()} was removed from {self.name.title()} Portfolio successfully."
        )

    def to_dict(self) -> dict:

        portfolio_dict = {
            "name": self.name,
            "cash": self.cash,
            "stock_asset_value": self.stock_asset_value,
            "unrealized_gain": self.unrealized_gain,
            "accounts": (
                [account.to_dict() for account in self.accounts.values()]
                if self.accounts
                else []
            ),
        }
        print("Portfolio dictionary successfully created!")
        return portfolio_dict
    
    def refresh_portfolio(self):
        print(f"Refreshing Portfolio: {self.name.title()}")
        updated_stock_asset_value = 0.0
        updated_unrealized_gain = 0.0
        updated_cash = 0.0
        for account in self.accounts.values():
            account.refresh_account()
            updated_stock_asset_value += account.stock_asset_value
            updated_unrealized_gain += account.unrealized_gain
            updated_cash += account.cash
        self._stock_asset_value = updated_stock_asset_value
        self._unrealized_gain = updated_unrealized_gain
        self._cash = updated_cash

        self.save_portfolio()
    


    def save_portfolio(self) -> None:
        temp_path = "app/database/portfolio.json"
        try:
            with open(temp_path, "w", newline="") as file:

                json.dump(self.to_dict(), file, indent=4)
                print("Portfolio successfully saved!")
        except FileNotFoundError:
            raise ValueError(
                "PortfolioError: Database file 'portfolio.json' does not exist."
            )

    @classmethod
    def load_portfolio(cls, file_path: str) -> Self:
        try:
            with open(file_path, "r", newline="") as portfolio_file:
                file_content = json.load(portfolio_file)

                loaded_portfolio = Portfolio(**file_content)
                converted_accounts = {}
                
                for account in loaded_portfolio.accounts:
                    loaded_account = Account.from_dict(account)
                    # set parent linkage
                    loaded_account._parent_portfolio = loaded_portfolio
                    converted_accounts[loaded_account.name] = loaded_account
                
                # overwrite the portfolio.accounts dict object structure with the converted accounts.
                loaded_portfolio.accounts = converted_accounts
                loaded_portfolio.refresh_portfolio()
                return loaded_portfolio
                
        except FileNotFoundError:
            raise ValueError(
                "PortfolioError: Database file 'portfolio.json' does not exist."
            )

    @classmethod
    def create_portfolio(cls, name: str) -> Self:
        new_portfolio = cls(name=name)
        return new_portfolio

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
