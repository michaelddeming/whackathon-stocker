import yfinance as yf
from Classes.Position import Position
from Classes.Account import Account
from Classes.Portfolio import Portfolio
from Classes.Transaction import Transaction

from PIL import Image


def main():

    # Create Portfolio Object
    test_portfolio = Portfolio(name="Deming Investments")

    # Create Account Object(s)
    test_account1 = Account(name="Individual Taxable", institution="Robinhood")
    test_account2 = Account(name="Roth IRA", institution="Fidelity")

    # Add Account(s) to Portfolio
    test_portfolio.add_accounts(test_account1, test_account2)

    # Create Position(s)
    test_position1 = Position(ticker="aapl", shares=1, average_cost=0)
    test_position2 = Position(ticker="msft", shares=10, average_cost=0)
    test_position3 = Position(ticker="pltr", shares=1, average_cost=0)

    # Add Position(s) to Account(s)
    test_account1.add_positions(test_position1, test_position2)
    test_account2.add_positions(test_position3)

    test_portfolio.save_portfolio()
    loaded_portfolio = Portfolio.load_portfolio("app/database/portfolio.json")
    print(loaded_portfolio.to_dict())
    test_portfolio.save_portfolio()




# try:
#     img = Image.open("app/assets/imgs/stocker_logo_full_dark.png")
#     img.show()
# except FileNotFoundError:
#     print("File not found.")

if __name__ == "__main__":
    main()
