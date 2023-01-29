from model2 import Darbininkai, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

session = sessionmaker(bind=engine)()

def naudotojo_meniu():
    print("=== [Darbuotojo apskaita] ===")
    print("1 | Prideti nauja darbuotoja")
    print("2 | Sarasas/perziura")
    print("3 | Pakeisti irasa")
    print("4 | Panaikinti irasa")
    print("0 | Iseiti")
    pasirinkimas = input("Pasirinkite veiksma: ")
    return pasirinkimas

def prideti_darbininka(vardas, pavarde, gimimo_data, pareigos, atlyginimas):
    darbininkas = Darbininkai(vardas, pavarde, gimimo_data, pareigos, atlyginimas)
    session.add(darbininkas)
    session.commit()
    print(darbininkas)
    return darbininkas

def prideti_nauja_darbuotoja_from_input():
    try:
        vardas = input("Vardas: ")
        pavarde = input("Pavarde: ")
        gimimo_data = datetime.strptime(input("Gimimo data (MMMM-MM-DD): "), "%Y-%m-%d")
        pareigos = input("Pareigos: ")
        atlyginimas = float(input("Atlyginimas: "))
    except ValueError:
        print("Error: Atlyginim1 nurodyti skaiciais")
    else:
        return prideti_darbininka(vardas, pavarde, gimimo_data, pareigos, atlyginimas)

def darbuotoju_sarasas(query=session.query(Darbininkai)):
    if len(query.all()) > 0:
        for darbuotojas in query.all():
            print(darbuotojas)
    else:
        print("--- Toks darbuotojas neegzistuoja ---")

def darbuotoju_paieska(query=session.query(Darbininkai)):
    paieska = input("Iveskite ko ieskote arba nieko, kad testumete")
    if not paieska:
        return
    try:
        query_atlyginimas = float(paieska)
    except ValueError:
        query = query.filter(Darbininkai.vardas.ilike(f"%{paieska}"))
    else:
        query = query.filter(Darbininkai.atlyginimas >= query_atlyginimas)
    finally:
        darbuotoju_sarasas(query)
        if len(query.all()) > 0:
            darbuotoju_paieska(query)
        else:
            darbuotoju_paieska()

def darbuotojo_istrinimas(darbuotojas):
    print(f"Panaikinamas darbuotojas {darbuotojas.id}...")
    session.delete(darbuotojas)
    session.commit()

def darbuotoju_sarasas_pagal_id():
    darbuotoju_sarasas()
    try:
        id = int(input("Iveskite darbuotojo ID: "))
    except ValueError:
        print("Error: darbuotojo ID turi buti skaicius")
    else:
        return session.query(Darbininkai).get(id)

def darbuotoju_saraso_atnaujinimas(darbuotojas, **pakeitimai):
    for column, value in pakeitimai.items():
        if value:
            setattr(darbuotojas, column, value)
    session.commit()
    print(darbuotojas)

def pakeitimu_pasirinkimas(darbuotojas):
    print(darbuotojas)
    print("Iveskite naujus duomenis arba iseikite")
    pakeitimai = {
        "vardas": input("Vardas: "),
        "pavarde": input("Pavarde: "),
        "pareigos": input("Pareigos: "),
        "atlyginimas": float(input("Atlyginimas: "))
    }
    return pakeitimai

while True:
    pasirinkimas = naudotojo_meniu()
    if pasirinkimas == "0" or pasirinkimas == "":
        break
    elif pasirinkimas == "1":
        prideti_nauja_darbuotoja_from_input()
    elif pasirinkimas == "2":
        darbuotoju_sarasas()
        darbuotoju_paieska()
    elif pasirinkimas == "3":
        darbuotojas = darbuotoju_sarasas_pagal_id()
        darbuotoju_saraso_atnaujinimas(darbuotojas, **pakeitimu_pasirinkimas(darbuotojas))
    elif pasirinkimas == "4":
        darbuotojo_istrinimas(darbuotoju_sarasas_pagal_id())
    else:
        print(f"Error: blogas pasirinkimas {pasirinkimas}")

