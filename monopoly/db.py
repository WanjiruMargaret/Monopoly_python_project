import sqlite3
import pickle
from player import Player

DB_NAME = "monopoly.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS players (
                name TEXT PRIMARY KEY,
                money INTEGER,
                position INTEGER,
                properties BLOB,
                in_jail INTEGER,
                jail_turns INTEGER
            )
        """)
        conn.commit()
    print("✅ Database setup complete!")

def save_player(player: Player):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO players (name, money, position, properties, in_jail, jail_turns)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(name) DO UPDATE SET
                money=excluded.money,
                position=excluded.position,
                properties=excluded.properties,
                in_jail=excluded.in_jail,
                jail_turns=excluded.jail_turns
        """, (
            player.name,
            player.money,
            player.position,
            pickle.dumps(player.properties),
            int(player.in_jail),
            player.jail_turns
        ))
        conn.commit()

def load_players():
    players = []
    with get_connection() as conn:
        cursor = conn.execute("SELECT name, money, position, properties, in_jail, jail_turns FROM players")
        for row in cursor.fetchall():
            name, money, position, properties_blob, in_jail, jail_turns = row
            p = Player(name, money)
            p.position = position
            p.properties = pickle.loads(properties_blob) if properties_blob else []
            p.in_jail = bool(in_jail)
            p.jail_turns = jail_turns
            players.append(p)
    return players
