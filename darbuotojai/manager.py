import sqlite3

conn = sqlite3.connect("data/darbuotojai.db")
c = conn.cursor()

while True:
<<<<<<< HEAD
    print("Iveskite nieko, kad iseiti")
    paieska = input("Ko ieskom?: ")
    if paieska == "":
        break
    else:
        paieska = f'%{paieska}%'
        with conn:
            #c.execute(f"SELECT * FROM darbuotojai WHERE pavarde LIKE '%{paieska}' OR vardas LIKE '%{paieska}%'")
=======
    print("Įveskite nieko kad išeiti")
    paieska = input("Ko ieškom?: ")
    if paieska == "":
        break
    else:
        paieska = f"%{paieska}%"
        with conn:
            # c.execute(f"SELECT * FROM darbuotojai WHERE pavarde LIKE '%{paieska}%' OR vardas LIKE '%{paieska}%'")
>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
            c.execute("SELECT * FROM darbuotojai WHERE pavarde LIKE ? OR vardas LIKE ?", (paieska, paieska))
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
