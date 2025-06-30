from .Position import Position

class Account:

    def __init__(self, name: str, institution: str):

        self.name = name
        self.institution = institution
        self.positions: dict[str, Position] = {}

    def add_position(self, position: Position):

        self.positions[position.ticker] = position
        print(f"{position.shares} share(s) of {position.ticker.upper()} added to {self.name} ({self.institution.title()}) successfully.")

    def delete_position(self, position:Position=None, ticker:str=None):
        
        if position:
            rem = self.positions.pop(position.ticker, None)
            if rem is None:
                raise KeyError("AccountError: Position not found, removal failed.")
            else:
                print(f"{position.ticker.upper()} removed from {self.name.title()} ({self.institution.title()}) successfully.")
        elif ticker:
            rem = self.positions.pop(ticker, None)
            if rem is None:
                raise KeyError("AccountError: Ticker not found, removal failed.")
            else:
                print(f"{ticker.upper()} removed from {self.name.title()}, {self.institution.title()} successfully.")
        else:
            raise ValueError("AccountError: Must provide a Position or ticker.")

    @property
    def total_value(self):
        if not self.positions:
            return 0.0
        total_value = 0.0
        for position in self.positions.values():
            total_value += position.total_value
        return total_value
    
    @property
    def unrealized_gain(self):
        if not self.positions:
            return 0.0
        total_gain = 0.0
        for position in self.positions.values():
            total_gain += position.unrealized_gain
        return total_gain
    





