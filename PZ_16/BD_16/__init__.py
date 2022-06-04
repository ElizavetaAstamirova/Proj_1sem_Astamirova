import sqlite3 as sq

with sq.connect('Anketa.db') as con:
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        add_FIO INTEGER NOT NULL DEFAULT 1,
        product TEXT NOT NULL,
        measurement TEXT NOT NULL,
        quantity TEXT NOT NULL,
        price INTEGER,
        nagr INTEGER NOT NULL DEFAULT 1,
        ad TEXT,
        spec TEXT
    )""")