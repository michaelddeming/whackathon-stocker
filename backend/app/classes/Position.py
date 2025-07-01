import yfinance as yf


class Position:

    def __init__(self, ticker: str, shares: float, average_cost: float):

        self.ticker = ticker.lower()
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

    def update(self, new_shares: float, new_average_cost: float):

        try:
            new_shares = float(new_shares)
        except ValueError:
            raise ValueError("PositionError: New share count type invalid.")

        if new_shares < 0:
            raise ValueError("PositionError: New share count must be 0+.")

        self.shares = new_shares

        try:
            new_average_cost = float(new_average_cost)
        except ValueError:
            raise ValueError("PositionError: New average cost type invalid.")

        if new_average_cost < 0:
            raise ValueError("PositionError: New average cost must be 0+.")

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