import sqlite3
from flask import Flask, request
app = Flask(__name__)

def db_connect():
    conn = None
    try:
        conn = sqlite3.connect('words.sqlite')
    except sqlite3.Error as error:
        print(error)
    return conn

@app.route('/words', methods=['POST'])
def word_list():
    word = request.form['word']
    meaning = request.form['meaning']
    language = request.form['language']
    english_translation = request.form['translation']
    example = request.form['example']

    conn = db_connect()
    c = conn.cursor()
    c.execute("INSERT INTO words (word, meaning, language, translated, example) VALUES (?,?,?,?,?)",
              (word, meaning, language, english_translation, example))
    conn.commit()
    conn.close()

    return "successfully saved data"

if __name__ == '__main__':
    app.run(debug=True)