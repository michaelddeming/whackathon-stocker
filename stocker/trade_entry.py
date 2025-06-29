"""
TradeEntry model for representing individual buy/sell transactions.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class TradeEntry(BaseModel):
    """Represents a single buy/sell transaction."""
    
    trade_id: str = Field(..., description="Unique trade identifier")
    ticker: str = Field(..., description="Stock/crypto ticker symbol")
    trade_type: str = Field(..., description="'buy' or 'sell'")
    shares: float = Field(..., description="Number of shares/units traded")
    price: float = Field(..., description="Price per share/unit")
    total_amount: float = Field(..., description="Total transaction amount")
    fees: float = Field(default=0.0, description="Transaction fees")
    trade_date: datetime = Field(..., description="When the trade occurred")
    notes: Optional[str] = Field(default=None, description="Optional trade notes")
