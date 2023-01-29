from sqlalchemy.orm import sessionmaker
from many2many import Tevas, Vaikas, engine

sesion = sessionmaker(bind=engine)()

#kestutis = Tevas(vardas="Kestutis", pavarde="Januskevicius")
#emilija = Vaikas(vardas="Emilija", pavarde="Januskeviciute")
#kestutis.vaikai.append(emilija)
#sesion.add(kestutis)
#sesion.commit()

#mama = Tevas(vardas="Nicoletta", pavarde="Januskeviciene")
#emilija = sesion.query(Vaikas).filter_by(vardas="Emilija").one()
#mama.vaikai.append(emilija)
#sesion.add(mama)
#sesion.commit()

tevai = sesion.query(Tevas).filter(Tevas.pavarde.ilike("Janus%")).all()
marco = Vaikas(vardas="Marco", pavarde="Januskevicius", tevai=tevai)
sesion.add(marco)
sesion.commit()