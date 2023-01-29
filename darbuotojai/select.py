import sqlite3

conn = sqlite3.connect("data/darbuotojai.db")
c = conn.cursor()

with conn:
    #c.execute("UPDATE darbuotojai SET vardas='Kestutis', pavarde='Bauzys' WHERE id=4;")
    #c.execute("DELETE FROM darbuotojai WHERE id=5;")
    c.execute("SELECT * FROM darbuotojai")

    c.execute("SELECT * FROM darbuotojai;")
    #darbuotojai = c.fetchall()
    while True:
        darbuotojas = c.fetchone()
        if darbuotojas:
            print(darbuotojas)
        else:
            break

#if darbuotojai:
    #print(darbuotojai)
