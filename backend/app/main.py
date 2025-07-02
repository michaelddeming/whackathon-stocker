import yfinance as yf
from classes.Position import Position
from classes.Account import Account
from classes.Portfolio import Portfolio


def main():

    test_portfolio = Portfolio(name="Deming Investments")
    test_account1 = Account(name="Individual Taxable", institution="Robinhood")

    
    test_portfolio.add_account(test_account1)

    
    test_position1 = Position(ticker="aapl", shares=23.865214, average_cost=199.12)
    print(test_position1.current_price)


    test_account1.add_position(test_position1)


    print(test_portfolio.total_value)
    print(test_portfolio.unrealized_gain)
        


if __name__ == "__main__":
    main()