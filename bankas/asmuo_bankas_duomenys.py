from asmuo_bankas import Asmuo, Bankas, Saskaita, engine
from sqlalchemy.orm import sessionmaker

sesion = sessionmaker(bind=engine)()

def naudotojo_meniu():
    print("=== MENIU ===")
    print("1 | Iveskite asmeni")
    print("2 | Iveskite banka")
    print("3 | Iveskite saskaita")
    print("4 | Iveskite pajamas/islaidas")
    print("5 | Perziureti asmenu sarasa")
    print("6 | Perziureti banku sarasa")
    print("7 | Perziureti saskaitu israsus")
    print("0 | Iseiti")
    pasirinkimas = input("Pasirinkite veiksma: ")
    return pasirinkimas

def ivesti_asmeni():
    asmens_ivedimas = Asmuo(vardas=input("Ivesti varda: "), pavarde=input("Ivesti pavarde: "), asmens_kodas=int(input("Ivesti asmens koda: ")), telefono_numeris=float(input("Ivesti telefono numeri: ")))
    sesion.add(asmens_ivedimas)
    sesion.commit()

def ivesti_banka():
    banko_ivedimas = Bankas(pavadinimas=input("Ivesti pavadinima: "), adresas=input("Ivesti adresa: "), banko_kodas=input("Ivesti banko koda: "), swift_kodas=input("Ivesti swift koda: "))
    sesion.add(banko_ivedimas)
    sesion.commit()

def ivesti_saskaita():
    asmenys = sesion.query(Asmuo).all()
    for asmuo in asmenys:
        print(asmuo.id, asmuo.vardas, asmuo.pavarde, asmuo.asmens_kodas)
    asmuo_id = int(input("Pasirinkite asmens ID: "))
    bankai = sesion.query(Bankas).all()
    for bankas in bankai:
        print(bankas.id, bankas.pavadinimas)
    bankas_id = int(input("Pasirinkite banko ID: "))
    saskaitos_ivedimas = Saskaita(saskaitos_nr=input("Ivesti saskaitos nr.: "), balansas=float(input("Ivesti: "), asmuo_id=asmuo_id, bankas_id=bankas_id))
    sesion.add(saskaitos_ivedimas)
    sesion.commit()

def ivesti_islaidas_pajamas():
    saskaitos = sesion.query(Saskaita).all()
    for saskaita in saskaitos:
        print(saskaita)
    saskaitos_id = int(input("Pasirinkite saskaitos ID: "))
    pasirinkta_saskaita = sesion.query(Saskaita).get(saskaitos_id)
    islaidos_pajamos = float(input("Ivesti pajamas/islaidas. Islaidas veskite su "-" zenklu"))
    pasirinkta_saskaita.balansas += islaidos_pajamos
    sesion.commit()

def asmenu_sarasas():
    asmenys = sesion.query(Asmuo).all()
    for asmuo in asmenys:
        print(asmuo)

def banku_sarasas():
    bankai = sesion.query(Bankas).all()
    for bankas in bankai:
        print(bankas)

def saskaitu_israsai():
    saskaitos = sesion.query(Saskaita).all()
    for saskaita in saskaitos:
        print(saskaita)

while True:
    pasirinkimas = naudotojo_meniu()
    if pasirinkimas == "0" or pasirinkimas == "":
        break
    elif pasirinkimas == "1":
        ivesti_asmeni()
    elif pasirinkimas == "2":
        ivesti_banka()
    elif pasirinkimas == "3":
        ivesti_saskaita()
    elif pasirinkimas == "4":
        ivesti_islaidas_pajamas()
    elif pasirinkimas == "5":
        asmenu_sarasas()
    elif pasirinkimas == "6":
        banku_sarasas()
    elif pasirinkimas == "7":
        saskaitu_israsai()