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

    # Create words database
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


# ============== ROUTES ==============

# Home route - serves the main HTML page
@app.route('/')
def index():
    return render_template('index.html')


# ============== PLAYERS CRUD ==============

# CREATE - Add a new player
@app.route('/api/players', methods=['POST'])
def create_player():
    try:
        data = request.get_json() if request.is_json else request.form

        username = data.get('username')
        slang = data.get('Slang', 0)
        rhyme = data.get('RhymeTime', 0)
        translate = data.get('Translate', 0)
        contextual = data.get('Contextual', 0)
        chain = data.get('Chain', 0)
        opposites = data.get('Opposites', 0)
        alpha = data.get('AlphaThon', 0)

        # Calculate average
        scores = [int(slang), int(rhyme), int(translate), int(contextual),
                  int(chain), int(opposites), int(alpha)]
        average = sum(scores) / len(scores) if scores else 0.0

        conn = get_db_connection('players.sqlite')
        c = conn.cursor()
        c.execute("""INSERT INTO players (username, Slang, RhymeTime, Translate, 
                     Contextual, Chain, Opposites, AlphaThon, Average) 
                     VALUES (?,?,?,?,?,?,?,?,?)""",
                  (username, slang, rhyme, translate, contextual, chain, opposites, alpha, average))
        conn.commit()
        player_id = c.lastrowid
        conn.close()

        return jsonify({"message": "Player created successfully", "id": player_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# READ - Get all players
@app.route('/api/players', methods=['GET'])
def get_players():
    try:
        conn = get_db_connection('players.sqlite')
        c = conn.cursor()
        c.execute("SELECT * FROM players")
        players = [dict(row) for row in c.fetchall()]
        conn.close()
        return jsonify(players), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# READ - Get a single player by ID
@app.route('/api/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    try:
        conn = get_db_connection('players.sqlite')
        c = conn.cursor()
        c.execute("SELECT * FROM players WHERE id = ?", (player_id,))
        player = c.fetchone()
        conn.close()

        if player:
            return jsonify(dict(player)), 200
        else:
            return jsonify({"error": "Player not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# UPDATE - Update a player
@app.route('/api/players/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    try:
        data = request.get_json() if request.is_json else request.form

        username = data.get('username')
        slang = data.get('Slang')
        rhyme = data.get('RhymeTime')
        translate = data.get('Translate')
        contextual = data.get('Contextual')
        chain = data.get('Chain')
        opposites = data.get('Opposites')
        alpha = data.get('AlphaThon')

        # Calculate new average
        scores = []
        for score in [slang, rhyme, translate, contextual, chain, opposites, alpha]:
            if score is not None:
                scores.append(int(score))
        average = sum(scores) / len(scores) if scores else None

        conn = get_db_connection('players.sqlite')
        c = conn.cursor()

        # Build dynamic UPDATE query
        update_fields = []
        values = []

        if username:
            update_fields.append("username = ?")
            values.append(username)
        if slang is not None:
            update_fields.append("Slang = ?")
            values.append(slang)
        if rhyme is not None:
            update_fields.append("RhymeTime = ?")
            values.append(rhyme)
        if translate is not None:
            update_fields.append("Translate = ?")
            values.append(translate)
        if contextual is not None:
            update_fields.append("Contextual = ?")
            values.append(contextual)
        if chain is not None:
            update_fields.append("Chain = ?")
            values.append(chain)
        if opposites is not None:
            update_fields.append("Opposites = ?")
            values.append(opposites)
        if alpha is not None:
            update_fields.append("AlphaThon = ?")
            values.append(alpha)
        if average is not None:
            update_fields.append("Average = ?")
            values.append(average)

        if update_fields:
            values.append(player_id)
            query = f"UPDATE players SET {', '.join(update_fields)} WHERE id = ?"
            c.execute(query, values)
            conn.commit()

        conn.close()
        return jsonify({"message": "Player updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# DELETE - Delete a player
@app.route('/api/players/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    try:
        conn = get_db_connection('players.sqlite')
        c = conn.cursor()
        c.execute("DELETE FROM players WHERE id = ?", (player_id,))
        conn.commit()
        conn.close()

        return jsonify({"message": "Player deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ============== WORDS CRUD ==============

# CREATE - Add a new word
@app.route('/api/words', methods=['POST'])
def create_word():
    try:
        data = request.get_json() if request.is_json else request.form

        word = data.get('word')
        meaning = data.get('meaning')
        language = data.get('language')
        translated = data.get('translated')
        example = data.get('example')

        conn = get_db_connection('words.sqlite')
        c = conn.cursor()
        c.execute("""INSERT INTO words (word, meaning, language, translated, example) 
                     VALUES (?,?,?,?,?)""",
                  (word, meaning, language, translated, example))
        conn.commit()
        word_id = c.lastrowid
        conn.close()

        return jsonify({"message": "Word created successfully", "id": word_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# READ - Get all words
@app.route('/api/words', methods=['GET'])
def get_words():
    try:
        conn = get_db_connection('words.sqlite')
        c = conn.cursor()
        c.execute("SELECT * FROM words")
        words = [dict(row) for row in c.fetchall()]
        conn.close()
        return jsonify(words), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# READ - Get a single word by ID
@app.route('/api/words/<int:word_id>', methods=['GET'])
def get_word(word_id):
    try:
        conn = get_db_connection('words.sqlite')
        c = conn.cursor()
        c.execute("SELECT * FROM words WHERE id = ?", (word_id,))
        word = c.fetchone()
        conn.close()

        if word:
            return jsonify(dict(word)), 200
        else:
            return jsonify({"error": "Word not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# UPDATE - Update a word
@app.route('/api/words/<int:word_id>', methods=['PUT'])
def update_word(word_id):
    try:
        data = request.get_json() if request.is_json else request.form

        word = data.get('word')
        meaning = data.get('meaning')
        language = data.get('language')
        translated = data.get('translated')
        example = data.get('example')

        conn = get_db_connection('words.sqlite')
        c = conn.cursor()

        # Build dynamic UPDATE query
        update_fields = []
        values = []

        if word:
            update_fields.append("word = ?")
            values.append(word)
        if meaning:
            update_fields.append("meaning = ?")
            values.append(meaning)
        if language:
            update_fields.append("language = ?")
            values.append(language)
        if translated:
            update_fields.append("translated = ?")
            values.append(translated)
        if example:
            update_fields.append("example = ?")
            values.append(example)

        if update_fields:
            values.append(word_id)
            query = f"UPDATE words SET {', '.join(update_fields)} WHERE id = ?"
            c.execute(query, values)
            conn.commit()

        conn.close()
        return jsonify({"message": "Word updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# DELETE - Delete a word
@app.route('/api/words/<int:word_id>', methods=['DELETE'])
def delete_word(word_id):
    try:
        conn = get_db_connection('words.sqlite')
        c = conn.cursor()
        c.execute("DELETE FROM words WHERE id = ?", (word_id,))
        conn.commit()
        conn.close()

        return jsonify({"message": "Word deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    # Initialize databases on startup
    init_databases()
    app.run(debug=True, host='0.0.0.0', port=5000)
