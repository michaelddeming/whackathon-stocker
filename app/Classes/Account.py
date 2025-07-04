from .Position import Position
from .Transaction import Transaction

class Account:

    def __init__(self, name: str, institution: str, parent_portfolio=None):

        self.name = name
        self.institution = institution
        self._parent_portfolio = parent_portfolio
        self._stock_asset_value = 0.0
        self._unrealized_gain = 0.0
        self._cash = 0.0
        self.positions: dict[str, Position] = {}

    def add_position(self, position: Position):
        # sync the Position to the account and set the Position name to include the institution.
        position._parent_account = self
        position.name = f"{position.ticker.upper()} | {self.name.title()}, {self.institution.title()}"
        
        # check if there is already a Position w/ ticker.
        already_found_position = self.positions.get(position.ticker, None)
        if already_found_position:
            raise ValueError(f"AccountError: {self.name.title()} already has a position for {position.ticker.upper()} stock of {position.shares} share(s) w/ an average cost of ${position.average_cost}.")
        # add Position to the positions data structure.
        self.positions[position.ticker] = position
        
        # increase the Account stock asset value and unrealized gain proportionally.
        self._stock_asset_value += position.total_value # Positon total_value = stock asset_value, there is not cash on Position
        self._unrealized_gain += position.unrealized_gain
        # print success message
        print(f"{position.shares} share(s) of {position.ticker.upper()} successfully added to {self.name} held with {self.institution.title()}.\n")
        
        # Push Position total_value and unrealized_gain to the Portfolio
        if self._parent_portfolio:
            self._parent_portfolio._stock_asset_value += position.total_value
            self._parent_portfolio._unrealized_gain += position.unrealized_gain
            print(f"Portfolio: {self._parent_portfolio.name.title()} successfully updated.\n")

        Transaction(transaction_type="add_position", amount=position.total_value, parent=self)
        
    def delete_position(self, position:Position=None, ticker:str=None):
        
        if position:
            rem = self.positions.pop(position.ticker, None)
        elif ticker:
            rem = self.positions.pop(ticker.lower(), None)
        else:
            raise ValueError("AccountError: Must provide a Position or ticker.")
        if rem is None:
            raise KeyError(f"AccountError: {(position.ticker if position else ticker).upper()} not found, removal failed.")
        self._stock_asset_value -= rem.total_value
        self._unrealized_gain -= rem.unrealized_gain
        print(f"{(position.ticker if position else ticker).upper()} removed successfully from {self.name.title()} held with {self.institution.title()}.\n")
        if self._parent_portfolio:
            self._parent_portfolio._stock_asset_value -= rem.total_value
            self._parent_portfolio._unrealized_gain -= rem.unrealized_gain
            print(f"Portfolio: {self._parent_portfolio.name.title()} successfully updated.\n")
    
    def overwrite_cash(self, new_cash: float):
        """Update the private Account._cash variable to a new positive value."""
        if new_cash < 0:
            raise ValueError("AccountError: Total cash value cannot be negative.")
        if new_cash == self.cash:
            raise ValueError("AccountError: Cash overwrite fail, new cash value is equal to old cash value.")
        current_cash = self.cash 

        self._cash = new_cash
        print(f"{self.name.title()} cash reserve successfully overwritten as ${new_cash}.\n")
        
        if self._parent_portfolio:
            self._parent_portfolio._cash -= current_cash
            self._parent_portfolio._cash += new_cash
            print(f"{self._parent_portfolio.name.title()} cash reserve successfully increased by ${new_cash - current_cash}.\n")

        

    def add_cash(self, cash_to_add: float):
        """Add a positive value of cash to the Account._cash variable."""

        if cash_to_add <= 0:
            raise ValueError("AccountError: Cash to add must be greater than $0.")
        self._cash += cash_to_add
        self._parent_portfolio._cash += cash_to_add
        print(f"Added ${cash_to_add:0.2f} successfully to {self.name.title()} cash reserve. New cash balance is ${self._cash:0.2f}\n")
    
    def delete_cash(self, cash_to_remove: float):
        """Remove a specified positive cash amount from the account reserve."""

        if cash_to_remove < 0:
            raise ValueError("AccountError: Cash to remove must be greater than $0.")
        if cash_to_remove > self._cash:
            raise ValueError(f"AccountError: Current cash balance, {self._cash:0.2f} not sufficient for removal of ${cash_to_remove:0.2f} from the {self.name.title()}.\n")
        
        self._parent_portfolio._cash -= cash_to_remove
        self._cash -= cash_to_remove
        print(f"Removed ${cash_to_remove:0.2f} successfully from {self.name.title()} cash reserve. New cash balance is {self._cash:0.2f}")

    @property
    def total_value(self):
        return self._stock_asset_value + self._cash
    
    @property
    def stock_asset_value(self):
        return self._stock_asset_value
    
    @property
    def unrealized_gain(self):
        return self._unrealized_gain

    @property
    def cash(self):
        return self._cash
