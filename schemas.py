from __future__ import annotations

from pydantic import BaseModel
from typing import Optional


class BetOut(BaseModel):
    id: Optional[int] = None
    sport: str = "football"
    datum_iso: Optional[str] = None
    datum: Optional[str] = None
    league: Optional[str] = None
    zapas: Optional[str] = None
    tip: Optional[str] = None
    market: Optional[str] = None
    kurz: Optional[float] = None
    prob_final: Optional[float] = None
    edge: Optional[float] = None
    vklad: Optional[float] = None
    bookmaker: Optional[str] = None
    result: Optional[str] = None
    created_at: Optional[str] = None


class PerformanceOut(BaseModel):
    settled: int
    wins: int
    losses: int
    win_rate: float
    turnover: float
    profit: float
    yield_pct: float
