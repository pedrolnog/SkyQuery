import sqlite3
import datetime as dt
from database.models import HistoryModel
from contextlib import contextmanager

@contextmanager
def get_connection():
    conn = sqlite3.connect("./app/database/astronomy.db", timeout=10)

    try:
        yield conn
    finally:
        conn.close()

def create_tables(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS history (ID INTEGER PRIMARY KEY, city TEXT, sunrise TEXT, sunset TEXT, day_length_seconds INTEGER NOT NULL, search_time DATETIME NOT NULL)")
    cursor.close()
    conn.commit()

def save_search(city: str, sunrise: str, sunset: str, day_length: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO history (id, city, sunrise, sunset, day_length_seconds, search_time) VALUES (NULL, ?, ?, ?, ?, ?)",
            (city.title(), sunrise, sunset, day_length, dt.datetime.now())
        )
        conn.commit()
        cursor.close()


def get_search_history(city: str | None = None) -> list[HistoryModel]:
    with get_connection() as conn:
        cursor = conn.cursor()

        if city:
            cursor.execute(
                "SELECT * FROM history WHERE city = ? ORDER BY id", (city.title(),)
            )
        else:
            cursor.execute(
                "SELECT * FROM history ORDER BY id"
            )

        history = cursor.fetchall()
        cursor.close()

        return [HistoryModel(
                id=item[0],
                city=item[1],
                sunrise=item[2],
                sunset=item[3],
                day_length_seconds=item[4],
                search_time=item[5],
            ) for item in history]