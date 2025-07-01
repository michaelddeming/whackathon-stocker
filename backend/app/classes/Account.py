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
            rem = self.positions.pop(ticker.lower(), None)
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
        return sum(position.total_value for position in self.positions.values())


    
    @property
    def unrealized_gain(self):
        if not self.positions:
            return 0.0
        return sum(position.unrealized_gain for position in self.positions.values())
    





