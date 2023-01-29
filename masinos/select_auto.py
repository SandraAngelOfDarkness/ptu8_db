import sqlite3

conn = sqlite3.connect("data/automobiliai.db")
c = conn.cursor()

with conn:
    c.execute("SELECT * FROM automobiliai;")
    while True:
        automobilis = c.fetchone()
        if automobilis:
            print(automobilis)
        else:
            break