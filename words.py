import sqlite3

conn = sqlite3.connect('words.sqlite')
c = conn.cursor()
sql_query = ("CREATE TABLE words("
             "id integer PRIMARY KEY, "
             "word text, "
             "meaning text, "
             "language text, "
             "translated text, "
             "example text"
             ")")

c.execute(sql_query)
