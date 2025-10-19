import sqlite3

conn = sqlite3.connect('players.sqlite')
c = conn.cursor()
sql_query = ("CREATE TABLE players("
             "id integer PRIMARY KEY, "
             "username text, "
             "Slang integer, "
             "RhymeTime integer, "
             "Translate integer, "
             "Contextual integer, "
             "Chain integer, "
             "Opposites integer, "
             "AlphaThon integer, "
             "Average float"
             ")")

c.execute(sql_query)
