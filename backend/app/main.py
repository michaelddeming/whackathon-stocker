import yfinance as yf
from classes.Position import Position


def main():
    
    test_position = Position(ticker="fzrox", shares=1, average_cost=0)
    test_position.update(update_key="shares",updated_value="5")
    test_position.update(update_key="average_cost",updated_value="10")
    print(test_position.average_cost)
    print(test_position.unrealized_gain)
    print(test_position.shares)



    


if __name__ == "__main__":
    main()