import sqlite3
import os

if not os.path.exists('data'):
    os.mkdir('data')

conn = sqlite3.connect('data/darbuotojai.db')
with conn:
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS darbuotojai (
            id INTEGER PRIMARY KEY NOT NULL,
            vardas VARCHAR(50) NOT NULL,
            pavarde VARCHAR(100) NOT NULL,
            atlyginimas DECIMAL(10,2)
        )
    """)
    #c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Giedrius', 'Isora', 555.55);")
    #c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Airida', 'Juraitiene', 666.66);")
    #c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Egle', 'Motiejunaite', 777.77);")
    #c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Daiva', 'Reinike', 888.88);")
    #c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Sandra', 'Krisiunaite', 999.99);")
    darbuotojai = [
        ('Egidijus', 'Jankunas', 1111),
        ('Gediminas', 'Zakas', 333),
        ('Ignas', 'Rocys', 123.45),
        ('Kevinas', 'Karpus', 987.67)
    ]
    c.executemany("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES (?, ?, ?)", darbuotojai)
