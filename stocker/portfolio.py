"""
Portfolio model for representing a user's complete investment portfolio.
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

from .account import Account
from .position import Position


class Portfolio(BaseModel):
    """Represents a user's complete investment portfolio."""
    
    user_id: str = Field(..., description="Unique user identifier")
    total_value: float = Field(..., description="Sum of all account values")
    cash_total: float = Field(..., description="Sum of all cash balances")
    accounts: List[Account] = Field(default_factory=list, description="All investment accounts")
    created_at: datetime = Field(default_factory=datetime.now, description="Portfolio creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.now, description="Last updated timestamp")
    
    def calculate_totals(self) -> tuple[float, float]:
        """Calculate and update total portfolio value and cash totals."""
        self.total_value = sum(account.total_value for account in self.accounts)
        self.cash_total = sum(account.cash_balance for account in self.accounts)
        self.updated_at = datetime.now()
        return self.total_value, self.cash_total
    
    def add_account(self, account: Account) -> None:
        """Add a new account to the portfolio."""
        self.accounts.append(account)
        self.updated_at = datetime.now()
    
    def get_account_by_id(self, account_id: str) -> Optional[Account]:
        """Find an account by its ID."""
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None
    
    def get_all_positions(self) -> List[Position]:
        """Get all positions across all accounts."""
        all_positions = []
        for account in self.accounts:
            all_positions.extend(account.positions)
        return all_positions
    
    def get_positions_by_ticker(self, ticker: str) -> List[Position]:
        """Get all positions for a specific ticker across all accounts."""
        positions = []
        for account in self.accounts:
            position = account.get_position_by_ticker(ticker)
            if position:
                positions.append(position)
        return positions
    
    def get_total_unrealized_gain(self) -> float:
        """Calculate total unrealized gain/loss across all positions."""
        return sum(position.unrealized_gain for position in self.get_all_positions())
