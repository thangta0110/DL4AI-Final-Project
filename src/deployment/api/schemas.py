"""Request/Response schemas for prediction API."""

from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime


class PredictionRequest(BaseModel):
    """Request schema for single prediction."""
    ticker: str
    days_ahead: int = 1
    window_size: int = 30
    model_type: str = "lstm"  # lstm, gru, transformer


class MultiDayPredictionRequest(BaseModel):
    """Request schema for multi-day forecast."""
    ticker: str
    k_days: int = 7
    window_size: int = 30
    model_type: str = "lstm"


class SignalRequest(BaseModel):
    """Request schema for trading signal."""
    ticker: str
    signal_type: str  # 'buy' or 'sell'
    threshold: float = 0.5


class PortfolioRequest(BaseModel):
    """Request schema for portfolio optimization."""
    tickers: List[str]
    profile: str = "prudent"  # prudent or risk-taking
    lookback_days: int = 120


class PredictionResponse(BaseModel):
    """Response schema for predictions."""
    ticker: str
    timestamp: datetime
    predicted_price: float
    confidence: float
    model_type: str
    days_ahead: int


class MultiDayPredictionResponse(BaseModel):
    """Response schema for multi-day predictions."""
    ticker: str
    timestamp: datetime
    predictions: List[Dict[str, float]]  # [{'day': x, 'price': y}, ...]
    model_type: str
    k_days: int


class SignalResponse(BaseModel):
    """Response schema for trading signals."""
    ticker: str
    timestamp: datetime
    signal: str  # 'buy', 'sell', 'hold'
    probability: float
    signal_type: str
    reasoning: Optional[str] = None


class PortfolioResponse(BaseModel):
    """Response schema for portfolio composition."""
    timestamp: datetime
    profile: str
    allocations: Dict[str, float]  # {ticker: weight}
    expected_return: float
    expected_risk: float
    compostion_details: Dict[str, Dict[str, float]]


class ModelHealthResponse(BaseModel):
    """Response schema for health check."""
    status: str  # healthy, degraded, error
    models_loaded: List[str]
    timestamp: datetime
    message: str
