"""
Account model for representing investment accounts (brokerage, 401k, crypto, etc.).
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

from .position import Position
from .trade_entry import TradeEntry


class Account(BaseModel):
    """Represents an investment account (brokerage, 401k, crypto, etc.)."""
    
    account_id: str = Field(..., description="Unique account identifier")
    account_type: str = Field(..., description="Account type (e.g., 'Brokerage', '401(k)', 'Crypto')")
    broker_name: str = Field(..., description="Broker/platform name (e.g., 'Robinhood', 'Fidelity')")
    cash_balance: float = Field(..., description="Available cash balance")
    total_value: float = Field(..., description="Cash + current positions value")
    positions: List[Position] = Field(default_factory=list, description="All current holdings")
    transactions: List[TradeEntry] = Field(default_factory=list, description="All buy/sell history")
    is_linked: bool = Field(default=False, description="Whether account is API-connected or manual entry")
    created_at: datetime = Field(default_factory=datetime.now, description="Account creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.now, description="Last update timestamp")
    
    def calculate_total_value(self) -> float:
        """Calculate and update total account value (cash + positions)."""
        positions_value = sum(position.total_value for position in self.positions)
        self.total_value = self.cash_balance + positions_value
        return self.total_value
    
    def add_position(self, position: Position) -> None:
        """Add a new position to the account."""
        self.positions.append(position)
        self.updated_at = datetime.now()
    
    def add_transaction(self, transaction: TradeEntry) -> None:
        """Add a new transaction to the account history."""
        self.transactions.append(transaction)
        self.updated_at = datetime.now()
    
    def get_position_by_ticker(self, ticker: str) -> Optional[Position]:
        """Find a position by ticker symbol."""
        for position in self.positions:
            if position.ticker == ticker:
                return position
        return None
