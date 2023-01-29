from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Project

engine = create_engine('sqlite:///data/projektai.db')
<<<<<<< HEAD
#Session = sessionmaker(bind=engine)
#session = Session()
session = sessionmaker(bind=engine)()

#CRUD = Create Read Update Delete
#Creat / INSERT
#naujas_projektas = Project('Brangus reikalas', 12000000000)
#kitas_projektas = Project('Geras puslapiukas', 50000)
#session.add(naujas_projektas)
#session.add(kitas_projektas)
#session.commit()

#Read / SELECT
#projektas1 = session.query(Project).get(2)
#projektas2 = session.query(Project).filter_by(name='Kiti reikalai').one()
#print(projektas2)
#projektai = session.query(Project).all()
#print(projektai)
#pigus_projektai = session.query(Project).filter(Project.price <= 10000).all()
#print(pigus_projektai)
#reikalai = session.query(Project).filter(Project.name.ilike("%reikala%")).all()
#print(reikalai)

#Update
#brangus = session.query(Project).filter(Project.price > 1000).first()
#brangus.price = 1000000
#session.commit()
#print(brangus)

#Delete
#projektas2 = session.query(Project).filter_by(name="Kiti reikalai").one()
#session.delete(projektas2)
#session.commit()
projektai = session.query(Project).all()
print(projektai)
=======
# Session = sessionmaker(bind=engine)
# session = Session()
session = sessionmaker(bind=engine)()

# CRUD = Create Read Update Delete
# Create / INSERT
# naujas_projektas = Project("Brangus Reikalas", 12000000)
# kitas_projektas = Project("Geras puslapiukas", 5000)
# session.add(naujas_projektas)
# session.add(kitas_projektas)
# session.commit()

# Read / SELECT
# projektas1 = session.query(Project).get(2)
# projektas2 = session.query(Project).filter_by(name="Kiti reikalai").one()
# print(projektas2)
# projektai = session.query(Project).all()
# print(projektai)
# pigus_projektai = session.query(Project).filter(Project.price <= 10000).all()
# print(pigus_projektai)
# reikalai = session.query(Project).filter(Project.name.ilike("%reikala%")).all()
# print(reikalai)

# Update
# brangus = session.query(Project).filter(Project.price > 100000).first()
# brangus.price = 1000000
# session.commit()
# print(brangus)

# Delete
# projektas2 = session.query(Project).filter_by(name="Kiti reikalai").one()
# session.delete(projektas2)
# session.commit()
projektai = session.query(Project).all()
print(projektai)
>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
