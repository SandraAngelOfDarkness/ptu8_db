import sqlite3

conn = sqlite3.connect("data/automobiliai.db")
c = conn.cursor()

while True:
    print("Spausti ENTER, kad iseiti")
    paieska = input("Iveskite norimus parametrus?: ")
    if paieska == "":
        break
    else:
        paieska = f'%{paieska}%'
        with conn:
            #c.execute(f"SELECT * FROM darbuotojai WHERE pavarde LIKE '%{paieska}' OR vardas LIKE '%{paieska}%'")
            c.execute("SELECT * FROM automobiliai WHERE marke LIKE ? OR modelis LIKE ? OR spalva LIKE?", (paieska, paieska, paieska))
            while True:
                automobilis = c.fetchone()
                if automobilis:
                    print(automobilis)
                else:
                    print("...daugiau nieko nera")
                    break
while True:
    print("Spausti Enter, kad iseiti")
    metai = input("Iveskite ieskomus metus: ")
    if metai == "":
        break
    else:
        metai = f'%{metai}%'
        with conn:
            c.execute("SELECT * FROM automobiliai where DATEDIFF LIKE (" "" - "" ")", (metai))
            break