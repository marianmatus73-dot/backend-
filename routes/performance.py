from __future__ import annotations

from fastapi import APIRouter

from backend.schemas import PerformanceOut
from backend.services.performance_service import get_performance

router = APIRouter(prefix="/performance", tags=["performance"])


@router.get("", response_model=PerformanceOut)
def performance():
    return get_performance()
