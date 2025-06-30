import datetime
import requests

class Position:

    def __init__(self, 
                 ticker: str,
                 shares: float,
                 average_cost: float,
                 current_price: float,
                 total_value: float,
                 unrealized_value: float,
                 tags: list[str],
                 notes: list[str]):
        
        self.ticker = ticker
        self.shares = shares
        self.average_cost = average_cost
        self.current_price = current_price
        self.total_value = total_value
        self.unrealized_value = unrealized_value
        self.tags = tags
        self.notes = notes

