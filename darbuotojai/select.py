import sqlite3

conn = sqlite3.connect("data/darbuotojai.db")
c = conn.cursor()

with conn:
<<<<<<< HEAD
    #c.execute("UPDATE darbuotojai SET vardas='Kestutis', pavarde='Bauzys' WHERE id=4;")
    #c.execute("DELETE FROM darbuotojai WHERE id=5;")
    c.execute("SELECT * FROM darbuotojai")

    c.execute("SELECT * FROM darbuotojai;")
    #darbuotojai = c.fetchall()
=======
    # c.execute("UPDATE darbuotojai SET vardas='Sandra', pavarde='Krisiūnaitė' WHERE id=3;")
    # c.execute("DELETE FROM darbuotojai WHERE id=4")
    c.execute("SELECT * FROM darbuotojai;")
    # darbuotojai = c.fetchall()
>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
    while True:
        darbuotojas = c.fetchone()
        if darbuotojas:
            print(darbuotojas)
        else:
            break

<<<<<<< HEAD
#if darbuotojai:
    #print(darbuotojai)
=======
# if darbuotojai:
#     print(darbuotojai)
>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
