"""
Example usage of the portfolio management models.

This file demonstrates how to create and use the Portfolio, Account, Position,
and TradeEntry classes.
"""

from datetime import datetime
from .portfolio import Portfolio
from .account import Account
from .position import Position
from .trade_entry import TradeEntry

def main():
    demonstrate_portfolio_operations()


def create_sample_portfolio() -> Portfolio:
    """Create a sample portfolio with accounts and positions."""
    
    # Create some sample trade entries
    trade1 = TradeEntry(
        trade_id="trade_001",
        ticker="AAPL",
        trade_type="buy",
        shares=10.0,
        price=150.00,
        total_amount=1500.00,
        fees=1.00,
        trade_date=datetime(2024, 1, 15),
        notes="Initial AAPL purchase"
    )
    
    trade2 = TradeEntry(
        trade_id="trade_002",
        ticker="TSLA",
        trade_type="buy",
        shares=5.0,
        price=200.00,
        total_amount=1000.00,
        fees=1.00,
        trade_date=datetime(2024, 2, 1),
        notes="Tesla investment"
    )
    
    # Create sample positions
    aapl_position = Position(
        ticker="AAPL",
        shares=10.0,
        avg_cost=150.00,
        current_price=175.00,
        total_value=1750.00,
        unrealized_gain=250.00,
        sector="Technology",
        tags=["large-cap", "dividend"],
        notes="Apple stock - solid dividend payer"
    )
    
    tsla_position = Position(
        ticker="TSLA",
        shares=5.0,
        avg_cost=200.00,
        current_price=180.00,
        total_value=900.00,
        unrealized_gain=-100.00,
        sector="Automotive",
        tags=["growth", "volatile"],
        notes="Tesla - high growth potential but volatile"
    )
    
    # Create a brokerage account
    brokerage_account = Account(
        account_id="acc_001",
        account_type="Brokerage",
        broker_name="Robinhood",
        cash_balance=500.00,
        total_value=3150.00,  # cash + positions
        positions=[aapl_position, tsla_position],
        transactions=[trade1, trade2],
        is_linked=True,
        created_at=datetime(2024, 1, 1),
        updated_at=datetime.now()
    )
    
    # Create crypto positions and account
    btc_position = Position(
        ticker="BTC-USD",
        shares=0.1,
        avg_cost=45000.00,
        current_price=50000.00,
        total_value=5000.00,
        unrealized_gain=500.00,
        sector="Cryptocurrency",
        tags=["crypto", "store-of-value"],
        notes="Bitcoin - digital gold"
    )
    
    crypto_account = Account(
        account_id="acc_002",
        account_type="Crypto",
        broker_name="Coinbase",
        cash_balance=100.00,
        total_value=5100.00,
        positions=[btc_position],
        transactions=[],
        is_linked=True,
        created_at=datetime(2024, 1, 15),
        updated_at=datetime.now()
    )
    
    # Create the portfolio
    portfolio = Portfolio(
        user_id="user_123",
        total_value=8250.00,  # sum of all accounts
        cash_total=600.00,    # sum of all cash
        accounts=[brokerage_account, crypto_account],
        created_at=datetime(2024, 1, 1),
        updated_at=datetime.now()
    )
    
    return portfolio


def demonstrate_portfolio_operations():
    """Demonstrate various portfolio operations."""
    
    print("Creating sample portfolio...")
    portfolio = create_sample_portfolio()
    
    print(f"Portfolio for user: {portfolio.user_id}")
    print(f"Total portfolio value: ${portfolio.total_value:,.2f}")
    print(f"Total cash: ${portfolio.cash_total:,.2f}")
    print(f"Number of accounts: {len(portfolio.accounts)}")
    
    print("\n--- Account Details ---")
    for account in portfolio.accounts:
        print(f"\nAccount: {account.account_id} ({account.account_type})")
        print(f"Broker: {account.broker_name}")
        print(f"Cash: ${account.cash_balance:,.2f}")
        print(f"Total Value: ${account.total_value:,.2f}")
        print(f"Positions: {len(account.positions)}")
        
        for position in account.positions:
            gain_loss = "gain" if position.unrealized_gain >= 0 else "loss"
            print(f"  - {position.ticker}: {position.shares} shares @ ${position.current_price:.2f}")
            print(f"    Unrealized {gain_loss}: ${abs(position.unrealized_gain):,.2f}")
    
    print("\n--- Portfolio Summary ---")
    all_positions = portfolio.get_all_positions()
    total_unrealized = portfolio.get_total_unrealized_gain()
    
    print(f"Total positions across all accounts: {len(all_positions)}")
    print(f"Total unrealized gain/loss: ${total_unrealized:,.2f}")
    
    # Demonstrate recalculating totals
    print("\n--- Recalculating Totals ---")
    new_total, new_cash = portfolio.calculate_totals()
    print(f"Recalculated total value: ${new_total:,.2f}")
    print(f"Recalculated cash total: ${new_cash:,.2f}")


if __name__ == "__main__":
    main()
