from .Position import Position

class Account:

    def __init__(self, name: str, institution: str):

        self.name = name
        self.institution = institution
        self._total_value = 0.0
        self._unrealized_gain = 0.0
        self.positions: dict[str, Position] = {}

    def add_position(self, position: Position):

        self.positions[position.ticker] = position
        self._total_value += position.total_value
        self._unrealized_gain += position.unrealized_gain
        print(f"{position.shares} share(s) of {position.ticker.upper()} added to {self.name} ({self.institution.title()}) successfully.")

    def delete_position(self, position:Position=None, ticker:str=None):
        
        if position:
            rem = self.positions.pop(position.ticker, None)
        elif ticker:
            rem = self.positions.pop(ticker.lower(), None)
        else:
            raise ValueError("AccountError: Must provide a Position or ticker.")
        if rem is None:
            raise KeyError(f"AccountError: {position.ticker if position else ticker} not found, removal failed.")
        self._total_value -= rem.total_value
        self._unrealized_gain -= rem.unrealized_gain
        print(f"{ticker.upper()} removed from {self.name.title()}, {self.institution.title()} successfully.")

    @property
    def total_value(self):
        return self._total_value
    
    @property
    def unrealized_gain(self):
        return self._unrealized_gain
    





