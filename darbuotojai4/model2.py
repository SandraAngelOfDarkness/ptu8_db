from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data/darbininkai.db')
Base = declarative_base()

class Darbininkai (Base):
    __tablename__ = "darbininkas"
    id = Column(Integer, primary_key = True)
    vardas = Column ("Vardas", String)
    pavarde = Column("Pavarde", String)
    gimimo_data = Column("Gimimo data", DateTime)
    pareigos = Column("Pareigos", String)
    atlyginimas = Column("Atlyginimas", Float)
    dirba_nuo = Column("Dirba nuo", DateTime, default=datetime.utcnow)

    def __init__(self, vardas, pavarde, gimimo_data, pareigos, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gimimo_data = gimimo_data
        self.pareigos = pareigos
        self.atlyginimas = atlyginimas

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde}, {self.gimimo_data}, {self.pareigos}, {self.atlyginimas}, {self.dirba_nuo})"

    def __str__(self):
        return f"darbininkas {self.vardas} {self.pavarde} su ID {self.id}, gimes {self.gimimo_data}, uzimantis {self.pareigos} pareigas, gaunantis {self.atlyginimas} atlyginima, pradejes dirbti {self.dirba_nuo}"

if __name__ == '__main__':
    Base.metadata.create_all(engine)