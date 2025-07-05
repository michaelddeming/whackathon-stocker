from .Classes.Portfolio import Portfolio

import json

def create_portfolio(name: str) -> Portfolio:

    """create a new/blank Portfolio object given the custom name string, set as Portfolio.name and return the Portfolio."""

    new_portfolio = Portfolio(name=name)
    # insert funciton write the Portfolio onto disk

    return new_portfolio


