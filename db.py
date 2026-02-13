import sqlite3

DB_NAME = "hack_sim.db"

def connect():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS player (
        id INTEGER PRIMARY KEY,
        money INTEGER
    )
    """)

    cur.execute("SELECT COUNT(*) FROM player")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO player (money) VALUES (0)")

    conn.commit()
    conn.close()

def get_money():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT money FROM player WHERE id=1")
    row = cur.fetchone()
    conn.close()
    return row[0] if row else 0

def add_money(amount):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE player SET money = money + ? WHERE id=1",
        (amount,)
    )
    conn.commit()
    conn.close()
