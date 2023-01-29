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
<<<<<<< HEAD
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
=======
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Giedrius', 'Išora', 5555.55);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Airida', 'Jūraitienė', 5555.55);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Eglė', 'Motiejūnaitė', 6666.66);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Daiva', 'Reinikė', 9999.99);")
    # c.execute("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES ('Kęstutis', 'Baužys', 7777.77);")
    darbuotojai = [
        ('Egidijus', 'Jankūnas', 0),
        ('Gediminas', 'Zakas', 10033.71),
        ('Ignas', 'Rocys', 6789.10),
        ('Kevinas', 'Karpus', 9876.54),
    ]
    c.executemany("INSERT INTO darbuotojai (vardas, pavarde, atlyginimas) VALUES (?, ?, ?)", darbuotojai)
    
>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
