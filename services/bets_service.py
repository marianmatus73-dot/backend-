from __future__ import annotations

from backend.database import get_connection


def get_today_bets(limit: int = 50) -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT
                id,
                'football' AS sport,
                datum_iso,
                datum,
                league,
                zapas,
                tip,
                market,
                kurz,
                prob_final,
                edge,
                vklad,
                bookmaker,
                result,
                created_at
            FROM bets
            WHERE result IS NULL OR result = ''
            ORDER BY datetime(datum_iso) ASC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    return [dict(row) for row in rows]


def get_recent_bets(limit: int = 100) -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT
                id,
                'football' AS sport,
                datum_iso,
                datum,
                league,
                zapas,
                tip,
                market,
                kurz,
                prob_final,
                edge,
                vklad,
                bookmaker,
                result,
                created_at
            FROM bets
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    return [dict(row) for row in rows]
