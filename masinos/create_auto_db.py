import sqlite3
import os

if not os.path.exists('data'):
    os.mkdir('data')

conn = sqlite3.connect('data/automobiliai.db')
with conn:
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS automobiliai (
            id INTEGER PRIMARY KEY NOT NULL,
            marke VARCHAR(50) NOT NULL,
            modelis VARCHAR(50) NOT NULL,
            spalva VARCHAR(50) NOT NULL,
            metai VARCHAR(50) NOT NULL,
            kaina DECIMAL(10,2)
        )
    """)
    #c.execute("INSERT INTO automobiliai (marke, modelis, spalva, metai, kaina) VALUES ('Opel', 'Signum', 'Juoda', '2005', 2099);")
    #c.execute("INSERT INTO automobiliai (marke, modelis, spalva, metai, kaina) VALUES ('BMW', '530', 'Melyna', '2001', 2100);")
    #c.execute("INSERT INTO automobiliai (marke, modelis, spalva, metai, kaina) VALUES ('Audi', 'A8', 'Pilka', '2005', 4300);")
    #c.execute("INSERT INTO automobiliai (marke, modelis, spalva, metai, kaina) VALUES ('Mazda', 'Premacy', 'Zalia', '2001', 490);")
    #c.execute("INSERT INTO automobiliai (marke, modelis, spalva, metai, kaina) VALUES ('Skoda', 'Yeti', 'Sidabrine', '2011', 5500);")
    