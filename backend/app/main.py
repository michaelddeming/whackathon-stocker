import yfinance as yf
from classes.Position import Position
from classes.Account import Account


def main():
    
    test_position1 = Position(ticker="aapl", shares=1, average_cost=0)
    test_position2 = Position(ticker="msft", shares=1, average_cost=0)

    test_account = Account(name="Roth IRA", institution="Fidelity")
    test_account.add_position(test_position1)
    test_account.add_position(test_position2)
    print(test_account.unrealized_gain)





    


if __name__ == "__main__":
    main()