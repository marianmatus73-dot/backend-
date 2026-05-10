from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.health import router as health_router
from backend.routes.bets import router as bets_router
from backend.routes.performance import router as performance_router


app = FastAPI(
    title="Multisport Betting API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(bets_router)
app.include_router(performance_router)


@app.get("/")
def root():
    return {
        "name": "Multisport Betting API",
        "status": "running",
    }
