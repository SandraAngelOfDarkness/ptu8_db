from sqlalchemy.orm import sessionmaker
from one2many import Tevas, Vaikas, engine

<<<<<<< HEAD

session = sessionmaker(bind=engine)()


print("--- Tevas su vaikais ---")
tevas = session.query(Tevas).filter(Tevas.vardas == "Kestutis").first()
print(tevas.vardas, tevas.pavarde, tevas.vaikai)
for vaikas in tevas.vaikai:
    print('-', vaikas.vardas, vaikas.pavarde)

print('---vaiko tevas---')
marco = session.query(Vaikas).filter(Vaikas.vardas == "Marco").first()
print(marco.vardas, "tevas yra", marco.tevas.vardas)

print("--- vaiko tevo antras vaikas pakoreguota pavarde ---")
#saraso elementai neturi visiskai jokios sasajos su ID
bauble = marco.tevas.vaikai[1]
bauble.pavarde = "Baublyte"
=======
session = sessionmaker(bind=engine)()

print('--- tevas su vaikais ---')
tevas = session.query(Tevas).filter(Tevas.vardas == "Kestutis").first()
print(tevas.vardas, tevas.pavarde)
for vaikas in tevas.vaikai:
    print('-', vaikas.vardas, vaikas.pavarde)

print('--- vaiko tevas ---')
marco = session.query(Vaikas).filter(Vaikas.vardas == "Marco").first()
print(marco.vardas, 'tevas yra', marco.tevas.vardas)

print('--- vaiko tevo antras vaikas pakoreguota pavarde ---')
# sąraši elementas neturi visisškai jokios sąsajos su ID
bauble = marco.tevas.vaikai[1]
bauble.pavarde = 'Baublytė'
>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
session.commit()
print(bauble.vardas, bauble.pavarde)

emilija = tevas.vaikai[0]
if emilija.vardas == "Emilija":
    tevas.vaikai.remove(emilija)
else:
<<<<<<< HEAD
    print("Emilija jau yra", emilija.vardas)
=======
    print('Emiljia jau yra ', emilija.vardas)
>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
session.commit()
