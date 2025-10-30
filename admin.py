import sqlite3
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Database connection helper
def get_db_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    except sqlite3.Error as error:
        print(f"Database error: {error}")
    return conn


# Initialize databases
def init_databases():
    # Create players database
    conn = get_db_connection('players.sqlite')
    if conn:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS players(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     username TEXT NOT NULL,
                     Slang INTEGER DEFAULT 0,
                     RhymeTime INTEGER DEFAULT 0,
                     Translate INTEGER DEFAULT 0,
                     Contextual INTEGER DEFAULT 0,
                     Chain INTEGER DEFAULT 0,
                     Opposites INTEGER DEFAULT 0,
                     AlphaThon INTEGER DEFAULT 0,
                     Average REAL DEFAULT 0.0
                     )""")
        conn.commit()
        conn.close()

        conn = get_db_connection('words.sqlite')
        if conn:
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS words(
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         word TEXT NOT NULL,
                         meaning TEXT,
                         language TEXT,
                         translated TEXT,
                         example TEXT
                         )""")
            conn.commit()
            conn.close()

@app.route('/')
def index():
    return render_template('index.html')