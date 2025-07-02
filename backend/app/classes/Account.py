from .Position import Position


class Account:

    def __init__(self, name: str, institution: str, parent_portfolio=None):

        self.name = name
        self.institution = institution
        self._parent_portfolio = parent_portfolio
        self._total_value = 0.0
        self._unrealized_gain = 0.0
        self.positions: dict[str, Position] = {}

    def add_position(self, position: Position):

        position._parent_account = self
        already_found_position = self.positions.get(position.ticker, None)
        if already_found_position:
            raise ValueError(f"AccountError: {self.name.title()} already has a position for {position.ticker.upper()} stock of {position.shares} share(s) w/ an average cost of ${position.average_cost}.")
        else:
            self.positions[position.ticker] = position
        self._total_value += position.total_value
        self._unrealized_gain += position.unrealized_gain
        print(f"{position.shares} share(s) of {position.ticker.upper()} successfully added to {self.name} held with {self.institution.title()}.\n")
        if self._parent_portfolio:
            self._parent_portfolio._total_value += position.total_value
            self._parent_portfolio._unrealized_gain += position.unrealized_gain
            print(f"Portfolio: {self._parent_portfolio.name.title()} successfully updated.\n")

    def delete_position(self, position:Position=None, ticker:str=None):
        
        if position:
            rem = self.positions.pop(position.ticker, None)
        elif ticker:
            rem = self.positions.pop(ticker.lower(), None)
        else:
            raise ValueError("AccountError: Must provide a Position or ticker.")
        if rem is None:
            raise KeyError(f"AccountError: {(position.ticker if position else ticker).upper()} not found, removal failed.")
        self._total_value -= rem.total_value
        self._unrealized_gain -= rem.unrealized_gain
        print(f"{(position.ticker if position else ticker).upper()} removed successfully from {self.name.title()} held with {self.institution.title()}.\n")
        if self._parent_portfolio:
            self._parent_portfolio._total_value -= rem.total_value
            self._parent_portfolio._unrealized_gain -= rem.unrealized_gain
            print(f"Portfolio: {self._parent_portfolio.name.title()} successfully updated.\n")

    @property
    def total_value(self):
        return self._total_value
    
    @property
    def unrealized_gain(self):
        return self._unrealized_gain





