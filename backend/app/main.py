import yfinance as yf
from classes.Position import Position


def main():
    
    test_position = Position(ticker="msft", shares=1, average_cost=0)

    print(test_position.unrealized_gain)
    

    
    


if __name__ == "__main__":
    main()