from sqlalchemy.orm import sessionmaker
from one2many import Tevas, Vaikas, engine


sesion = sessionmaker(bind=engine)()


kestutis = Tevas(vardas="Kestutis", pavarde="Januskevicius")
emilija = Vaikas(vardas="Emilija", pavarde="Januskeviciute")
maja = Vaikas(vardas="Maja", pavarde="Januskeviciute")
marco = Vaikas(vardas="Marco", pavarde="Januskevicius")

#trecias
#emilija.tevas = kestutis
#maja.tevas = kestutis
#marco.tevas = kestutis
#sesion.add(emilija)
#sesion.add(maja)
#sesion.add(marco)

#alternatyviai, jeigu nera kitu vaiku
#kestutis.vaikai = [emilija, maja, marco]
#sesion.add(kestutis)

#pirmas
kestutis.vaikai.append(emilija)
kestutis.vaikai.append(maja)
kestutis.vaikai.append(marco)
sesion.add(kestutis)

sesion.commit()