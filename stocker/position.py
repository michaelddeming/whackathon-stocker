"""
Position model for representing current holdings in an investment account.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class Position(BaseModel):
    """Represents a current holding in an investment account."""
    
    ticker: str = Field(..., description="Stock/crypto ticker symbol (e.g., 'AAPL', 'ETH-USD')")
    shares: float = Field(..., description="Number of shares or units held")
    avg_cost: float = Field(..., description="Average cost per share/unit")
    current_price: float = Field(..., description="Latest market price")
    total_value: float = Field(..., description="shares * current_price")
    unrealized_gain: float = Field(..., description="(current_price - avg_cost) * shares")
    sector: Optional[str] = Field(default=None, description="Sector classification (e.g., 'Tech', 'Healthcare')")
    tags: List[str] = Field(default_factory=list, description="User-defined tags (e.g., ['growth', 'dividend'])")
    notes: Optional[str] = Field(default=None, description="Freeform user notes")
    
    def calculate_total_value(self) -> float:
        """Calculate and update total value based on current price and shares."""
        self.total_value = self.shares * self.current_price
        return self.total_value
    
    def calculate_unrealized_gain(self) -> float:
        """Calculate and update unrealized gain/loss."""
        self.unrealized_gain = (self.current_price - self.avg_cost) * self.shares
        return self.unrealized_gain
