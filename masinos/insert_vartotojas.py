import sqlite3

conn = sqlite3.connect("data/automobiliai.db")
c = conn.cursor()

while True:
    print("Spauskite ENTER, jei norite iseiti")
    ivedimas = input("Pasirinkite veiksma: \n1-naujos auto ivedimas \n2-auto paieska \nVEIKSMAS \2: ")
    if ivedimas == "":
        break
    if ivedimas == "1":
        i_marke = input("Iveskite auto marke: ")
        i_modelis = input("Iveskite auto modeli: ")
        i_spalva = input("Iveskite auto spalva: ")
        i_metai = input("Iveskite auto pagaminimo metus: ")
        i_kaina = input("Iveskite pardavimo kaina: ")

        c.execute("INSERT INTO automobiliai (marke, modelis, spalva, metai, kaina) VALUES (?, ?, ?, ?, ?)", (i_marke, i_modelis, i_spalva, i_metai, i_kaina))
        conn.commit()
        print("Jusu duomenys ivesti")

    if ivedimas == "2":
        p_marke = input("Iveskite auto marke: ")
        p_modelis = input("Iveskite auto modeli: ")
        p_spalva = input("Iveskite auto spalva: ")
        p_metai_nuo = input("Iveskite metus nuo: ")
        p_metai_iki = input("Iveskite metus iki: ")
        p_kaina_nuo = input("Iveskite kaina nuo: ")
        p_kaina_iki = input("Iveskite kaina iki: ")
        p_marke = f"%{p_marke}%"
        p_modelis = f"%{p_modelis}"
        p_spalva = f"%{p_spalva}"
        select = "SELECT * FROM automobiliai WHERE marke LIKE ? AND modelis LIKE ? AND spalva LIKE ?"
        args = [p_marke, p_modelis, p_spalva]
        if p_metai_nuo:
            select += "AND p_metai >= ?"
            args.append(p_metai_nuo)
        if p_metai_iki:
            select -= "AND p_metai <= ?"
            args.append(p_metai_iki)
        if p_kaina_nuo:
            select += "AND p_kaina >= ?"
            args.append(p_kaina_nuo)
        if p_kaina_iki:
            select -= "AND p_kaina <= ?"
            args.append(p_kaina_iki)
        with conn:
            c.execute(select, args)
            while True:
                automobiliai = c.fetchone()
                if automobiliai:
                    print(automobiliai)
                else:
                    print("Paieska baigta")
                    break
                