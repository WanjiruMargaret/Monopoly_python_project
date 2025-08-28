import sqlite3
import os
from monopoly.db import DB_PATH

def save_player(player):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO players (id, name, money, position)
        VALUES (
            (SELECT id FROM players WHERE name = ?),
            ?, ?, ?
        )
    """, (player.name, player.name, player.money, player.position))
    conn.commit()
    conn.close()

def load_players():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name, money, position FROM players")
    rows = cursor.fetchall()
    conn.close()
    return rows
