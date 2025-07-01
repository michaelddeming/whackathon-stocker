import yfinance as yf
from classes.Position import Position
from classes.Account import Account
from classes.Portfolio import Portfolio


def main():
    test_portfolio = Portfolio(name="Michael Deming")
    test_account1 = Account(name="Roth IRA", institution="Fidelity")
    test_account2 = Account(name="Traditional IRA", institution="Robinhood")
    
    test_portfolio.add_account(test_account1)
    test_portfolio.add_account(test_account2)
    
    test_position1 = Position(ticker="aapl", shares=1, average_cost=0)
    test_position2 = Position(ticker="aapl", shares=1, average_cost=0)
    test_position3 = Position(ticker="aapl", shares=1, average_cost=0)
    test_position4 = Position(ticker="aapl", shares=1, average_cost=0)
    


    test_account1.add_position(test_position1)
    test_account1.add_position(test_position2)
    test_account2.add_position(test_position3)
    test_account2.add_position(test_position4)
    


    print(test_portfolio.total_value)
    test_position1.update(new_shares=1, new_average_cost=200)
    print(test_portfolio.total_value)
    print(test_portfolio.unrealized_gain)
    test_position2.update(new_shares=1, new_average_cost=10)
    print(test_portfolio.total_value)
    print(test_portfolio.unrealized_gain)

    
    # print(test_account1.total_value)
    # print(test_account2.total_value)
    # print(test_account1.unrealized_gain)
    # print(test_account2.unrealized_gain)





    


if __name__ == "__main__":
    main()