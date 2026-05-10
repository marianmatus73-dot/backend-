from __future__ import annotations

from fastapi import APIRouter, Query

from backend.schemas import BetOut
from backend.services.bets_service import get_today_bets, get_recent_bets

router = APIRouter(prefix="/bets", tags=["bets"])


@router.get("/today", response_model=list[BetOut])
def today_bets(limit: int = Query(50, ge=1, le=200)):
    return get_today_bets(limit=limit)


@router.get("/recent", response_model=list[BetOut])
def recent_bets(limit: int = Query(100, ge=1, le=500)):
    return get_recent_bets(limit=limit)
