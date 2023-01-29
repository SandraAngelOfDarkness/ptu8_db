import sqlite3

conn = sqlite3.connect("data/darbuotojai.db")
c = conn.cursor()

while True:
<<<<<<< HEAD
    print("Atskirimas kableliais, nieko kad iseiti")
    paieska = input("Iveskite ID: ")
=======
    print("Atskyrimas kableliais, nieko kad išeiti")
    paieska = input("Įveskite ID: ")
>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
    if paieska == "":
        break
    else:
        ids = paieska.split(',')
        with conn:
<<<<<<< HEAD
            #c.execute(f"SELECT * FROM darbuotojai WHERE pavarde LIKE '%{paieska}' OR vardas LIKE '%{paieska}%'")
            query = "SELECT * FROM darbuotojai WHERE rowid IN ("+', '.join(['?' for x in range(len(ids))])+")"
=======
            # c.execute(f"SELECT * FROM darbuotojai WHERE pavarde LIKE '%{paieska}%' OR vardas LIKE '%{paieska}%'")
            query = "SELECT * FROM darbuotojai WHERE rowid IN (" + ', '.join(['?' for _ in range(len(ids))]) + ")"
>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
            print(query)
            c.execute(query, ids)
            while True:
                darbuotojas = c.fetchone()
                if darbuotojas:
                    print(darbuotojas)
                else:
<<<<<<< HEAD
                    print("...daugiau nieko nera")
                    break
=======
                    print("...daugiau nieko nėra")
                    break
>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
