from sqlalchemy.orm import sessionmaker
from many2many import Tevas, Vaikas, engine

<<<<<<< HEAD

sesion = sessionmaker(bind=engine)()

print("--- tevas su vaikais ---")
tevas = sesion.query(Tevas).filter_by(vardas="Kestutis").one()
print(tevas.vardas, tevas.pavarde)
for vaikas in tevas.vaikai:
    print("-", vaikas.vardas, vaikas.pavarde)

mama = sesion.query(Tevas).filter_by(vardas="Nicoletta").one()
print(mama.vardas, mama.pavarde)
for vaikas in mama.vaikai:
    print("-", vaikas.vardas, vaikas.pavarde)

print("--- vaikas su tevais ---")
emilija = sesion.query(Vaikas).filter_by(vardas="Emilija").one()
print(emilija.vardas, emilija.pavarde)
for emilijos_tevas in emilija.tevai:
    print("-", emilijos_tevas.vardas, emilijos_tevas.pavarde)

maja = sesion.query(Vaikas).filter_by(vardas="Maja").one()
print(maja.vardas, maja.pavarde)
for majos_tevas in maja.tevai:
    print("-", majos_tevas.vardas, majos_tevas.pavarde)

marco = sesion.query(Vaikas).filter_by(vardas="Marco").one()
print(marco.vardas, marco.pavarde)
for marco_tevas in marco.tevai:
    print("-", marco_tevas.vardas, marco_tevas.pavarde)

#jei daug irasu
#print("--- vaikas su tevais ---")
#vaikai = sesion.query(Vaikas).all()
#for vaikas in vaikai:
    #print(vaikas.vardas, vaikas.pavarde)
    #for vaiko_tevas in vaikas.tevai:
        #print("-", vaiko_tevas.vardas, vaiko_tevas.pavarde)
=======
session = sessionmaker(bind=engine)()

print('--- tevai su vaikais ---')
tevas = session.query(Tevas).filter_by(vardas="Kestutis").one()
print(tevas.vardas, tevas.pavarde)
for vaikas in tevas.vaikai:
    print('-', vaikas.vardas, vaikas.pavarde)

mama = session.query(Tevas).filter_by(vardas="Nicoletta").one()
print(mama.vardas, mama.pavarde)
for vaikas in mama.vaikai:
    print('-', vaikas.vardas, vaikas.pavarde)

print('--- vaikai su tevais ---')
vaikai = session.query(Vaikas).all()
for vaikas in vaikai:
    print(vaikas.vardas, vaikas.pavarde)
    for vaiko_tevas in vaikas.tevai:
        print('-', vaiko_tevas.vardas, vaiko_tevas.pavarde)
>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
