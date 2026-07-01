import sqlite3
import os

DB = os.path.join(os.path.dirname(__file__), "..", "posto.db")

def conectar():
    conn = sqlite3.connect("posto.db", timeout=10)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def criar_tabelas():
    conn = conectar()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS combustiveis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        preco REAL,
        tipo TEXT,
        aditivada INTEGER,
        origem TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS bombas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero INTEGER,
        combustivel_id INTEGER,
        FOREIGN KEY (combustivel_id) REFERENCES combustiveis(id)
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS abastecimentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bomba_id INTEGER,
        combustivel_id INTEGER,
        litros REAL,
        valor REAL,
        data TEXT
    )
    """)

    conn.commit()
    conn.close()