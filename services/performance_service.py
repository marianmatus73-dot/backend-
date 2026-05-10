from __future__ import annotations

from backend.database import get_connection


def get_performance() -> dict:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT kurz, vklad, result
            FROM bets
            WHERE result IN ('V', 'P')
            """
        ).fetchall()

    settled = len(rows)
    wins = sum(1 for r in rows if r["result"] == "V")
    losses = sum(1 for r in rows if r["result"] == "P")

    turnover = 0.0
    profit = 0.0

    for row in rows:
        kurz = float(row["kurz"] or 0)
        vklad = float(row["vklad"] or 0)

        turnover += vklad

        if row["result"] == "V":
            profit += vklad * (kurz - 1.0)
        else:
            profit -= vklad

    win_rate = wins / settled if settled else 0.0
    yield_pct = profit / turnover if turnover else 0.0

    return {
        "settled": settled,
        "wins": wins,
        "losses": losses,
        "win_rate": round(win_rate, 4),
        "turnover": round(turnover, 2),
        "profit": round(profit, 2),
        "yield_pct": round(yield_pct, 4),
    }
