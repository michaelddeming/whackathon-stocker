import yfinance as yf
from classes.Position import Position
from classes.Account import Account
from classes.Portfolio import Portfolio


def main():

    test_portfolio = Portfolio(name="Deming Investments")
    test_account1 = Account(name="Individual Taxable", institution="Robinhood")
    test_portfolio.add_account(test_account1)
    test_account2 = Account(name="Roth IRA", institution="Fidelity")
    test_portfolio.add_account(test_account2)

    
    test_position1 = Position(ticker="aapl", shares=1, average_cost=0)
    test_account1.add_position(test_position1)
    test_position2 = Position(ticker="aapl", shares=1, average_cost=0)
    test_account2.add_position(test_position2)


    print(test_account1.total_value)
    print(test_account1.stock_asset_value)
    print(test_account1.cash)

    test_account1.add_cash(100)
    test_account2.add_cash(100)

    print(test_account1.total_value)
    print(test_account1.stock_asset_value)
    print(test_account1.cash)
    print()
    print(test_portfolio.stock_asset_value)
    print(test_portfolio.cash)
    print(test_portfolio.total_value)


        


if __name__ == "__main__":
    main()