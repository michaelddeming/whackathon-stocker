import yfinance as yf


class Position:

    def __init__(self, ticker: str, shares: float, average_cost: float):

        self.ticker = ticker
        self.shares = float(shares)
        self.average_cost = float(average_cost)

    def get_info(self, info_key: str) -> None:
        """
        Fetch specific market information for the current ticker using yfinance.

        Parameters:
            info_key (str): The type of information to retrieve.
                            Supported values: 'current_price', 'sector'.

        Returns:
            float or str: The requested value (e.g., current price or sector name).

        Raises:
            ValueError: If the ticker data is unavailable, the key is invalid,
                        or the requested field is not found in the ticker info.
        """

        ticker_info = yf.Ticker(self.ticker).info
        if not ticker_info:
            raise ValueError("PositionError: No ticker data.")
        match info_key:
            case "current_price":
                try:
                    current_price = ticker_info["regularMarketPrice"]
                except KeyError:
                    raise ValueError("PositionError: Current Price Not Found.")
                return current_price
            case "sector":
                try:
                    current_sector = ticker_info["sector"]
                except KeyError:
                    raise ValueError("PositionError: Sector Not Found.")
                return current_sector
            case _:
                raise ValueError("PositionError: Invalid Info Key.")

    def update(self, update_key: str, updated_value):
        update_keys = {"shares", "average_cost"}

        if update_key not in update_keys:
            raise ValueError("PositionError: Invalid Update Key.")

        match update_key:
            case "shares":
                try:
                    new_shares = float(updated_value)
                except ValueError:
                    raise ValueError("PositionError: Share count type invalid.")

                if new_shares < 0:
                    raise ValueError("PositionError: Share count must be 0+.")

                self.shares = new_shares

            case "average_cost":
                try:
                    new_average_cost = float(updated_value)
                except ValueError:
                    raise ValueError("PositionError: Average Cost type invalid.")

                if new_average_cost < 0:
                    raise ValueError("PositionError: Average Cost must be 0+.")

                self.average_cost = new_average_cost

    @property
    def current_price(self):
        return self.get_info("current_price")
    @property
    def sector(self):
        return self.get_info("sector")
    @property
    def total_value(self):
        return self.current_price * self.shares
    @property
    def unrealized_gain(self):
        return (self.current_price - self.average_cost) * self.shares