from model3 import Asmenys, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

sesion = sessionmaker(bind=engine)()

def add_record(vardas, pavarde, amzius, pareigos):
    asmuo = Asmenys(vardas, pavarde, amzius, pareigos)
    sesion.add(asmuo)
    sesion.commit()

def update_record(record_id, naujas_vardas, nauja_pavarde, naujas_amzius, naujos_pareigos):
    asmuo = sesion.query(Asmenys).get(record_id)
    asmuo.vardas = naujas_vardas
    asmuo.pavarde = nauja_pavarde
    asmuo.amzius = naujas_amzius
    asmuo.pareigos = naujos_pareigos
    sesion.commit()

def delete_record(record_id):
    asmuo = sesion.query(Asmenys).get(record_id)
    sesion.delete(asmuo)
    sesion.commit()

def get_all_records_list():
    return sesion.query(Asmenys).all()
