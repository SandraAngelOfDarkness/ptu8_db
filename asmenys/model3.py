from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data/asmenys.db')
Base = declarative_base()

class Asmenys (Base):
    __tablename__ = "zmogus"
    id = Column(Integer, primary_key = True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavarde", String)
    amzius = Column("Amzius", Integer)
    pareigos = Column("Pareigos", String)

    def __init__(self, vardas, pavarde, amzius, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.amzius = amzius
        self.pareigos = pareigos

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde}, {self.amzius}, {self.pareigos}"

    def __str__(self):
        return f"asmuo {self.vardas} {self.pavarde} turinti(-s) ID {self.id} {self.amzius} amziaus, dirbanti(-s) {self.pareigos}"

if __name__ == '__main__':
    Base.metadata.create_all(engine)