import yfinance as yf
from Classes.Position import Position
from Classes.Account import Account
from Classes.Portfolio import Portfolio
from Classes.Transaction import Transaction


def main():

    # Create Portfolio Object
    test_portfolio = Portfolio(name="Deming Investments")

    # Create Account Object(s)
    test_account1 = Account(name="Individual Taxable", institution="Robinhood")
    test_account2 = Account(name="Roth IRA", institution="Fidelity")

    # Add Account(s) to Portfolio
    test_portfolio.add_account(test_account1)
    test_portfolio.add_account(test_account2)

    # Create Position(s)
    test_position1 = Position(ticker="aapl", shares=1, average_cost=213.55)
    test_position2 = Position(ticker="aapl", shares=1, average_cost=213.55)

    # Add Position(s) to Account(s)
    test_account1.add_position(test_position1)
    test_account2.add_position(test_position2)

    
    print(test_portfolio.stock_asset_value)
    print(test_portfolio.cash)
    print(test_portfolio.total_value)
    print(test_portfolio.unrealized_gain)


if __name__ == "__main__":
    main()
