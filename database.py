import sqlite3
from flask import Flask, request
app = Flask(__name__)


def db_connect():
    conn = None
    try:
        conn = sqlite3.connect('players.sqlite')
    except sqlite3.Error as error:
        print(error)
    return conn


@app.route('/players', methods=['POST'])
def player_data():
    name = request.form['name']
    slang_hs = request.form['Slang high score']
    rhyme_hs = request.form['Rhyme Time high score']
    translate_hs = request.form['Translate high score']
    context_hs = request.form['Contextual high score']
    chain_hs = request.form['Chain high score']
    opposite_hs = request.form['Opposites high score']
    alpha_hs = request.form['Alpha-Thon high score']
    average = request.form['Average high score']

    conn = db_connect()
    c = conn.cursor()
    c.execute("""INSERT INTO players (name, slang, rhyme, translate, context, chain, oppo, alpha, average) 
    VALUES (?,?,?,?,?,?,?,?,?)""", (name, slang_hs, rhyme_hs, translate_hs, context_hs,
                                    chain_hs, opposite_hs, alpha_hs, average))
    conn.commit()
    conn.close()

    return "successfully saved data"


if __name__ == '__main__':
    app.run(debug=True)
