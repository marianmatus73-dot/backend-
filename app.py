from __future__ import annotations

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any

from fastapi import FastAPI

app = FastAPI(
    title="Multisport Betting API",
    version="0.1.0",
)

ROOT = Path(__file__).resolve().parents[1]
DB_FILE = ROOT / "bets.db"
EXPORTS_DIR = ROOT / "exports"


def read_latest_json_export() -> list[dict[str, Any]]:
    if not EXPORTS_DIR.exists():
        return []

    files = sorted(
        EXPORTS_DIR.glob("*.json"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )

    if not files:
        return []

    try:
        return json.loads(files[0].read_text(encoding="utf-8"))
    except Exception:
        return []


@app.get("/")
def root() -> dict[str, str]:
    return {
        "app": "Multisport Betting API",
        "status": "ok",
    }


@app.get("/health")
def health() -> dict[str, Any]:
    return {
        "status": "ok",
        "db_exists": DB_FILE.exists(),
        "exports_exists": EXPORTS_DIR.exists(),
        "time": datetime.utcnow().isoformat(),
    }


@app.get("/bets/latest")
def latest_bets() -> list[dict[str, Any]]:
    return read_latest_json_export()


@app.get("/bets/today")
def today_bets() -> list[dict[str, Any]]:
    bets = read_latest_json_export()

    today = datetime.utcnow().date().isoformat()

    out = []

    for bet in bets:
        datum_iso = str(bet.get("datum_iso", ""))

        if datum_iso.startswith(today):
            out.append(bet)

    return out


@app.get("/performance")
def performance() -> dict[str, Any]:
    if not DB_FILE.exists():
        return {
            "settled": 0,
            "wins": 0,
            "losses": 0,
            "profit": 0.0,
            "turnover": 0.0,
            "yield": 0.0,
            "win_rate": 0.0,
        }

    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row

    rows = conn.execute(
        """
        SELECT kurz, vklad, result
        FROM bets
        WHERE result IN ('V', 'P')
        """
    ).fetchall()

    conn.close()

    settled = len(rows)
    wins = 0
    losses = 0
    profit = 0.0
    turnover =
