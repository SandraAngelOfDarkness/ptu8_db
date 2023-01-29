from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/banko_saskaitos.db')
Base = declarative_base()


class Asmuo(Base):
    __tablename__ = "asmuo"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavarde", String)
    asmens_kodas = Column("Asmens kodas", Integer, unique=True)
    telefono_numeris = Column("Telefono nr", Float)
    saskaitos = relationship("Saskaita", back_populates="bankas")


class Bankas(Base):
    __tablename__ = "bankas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("Pavadinimas", String)
    adresas = Column("Adresas", String)
    banko_kodas = Column("Banko kodas", Integer)
    swift_kodas = Column("SWIFT kodas", String)
    saskaitos = relationship("Saskaita", back_populates="asmuo")


class Saskaita(Base):
    __tablename__ = "saskaita"
    id = Column(Integer, primary_key=True)
    numeris = Column("Saskaitos nr", Integer, unique=True)
    balansas = Column("Balansas", Float)
    asmuo_id = Column("asmuo_id", Integer, ForeignKey("asmuo.id"))
    asmuo = relationship("Asmuo", back_populates="saskaitos")
    bankas_id = Column("bankas_id", Integer, ForeignKey("bankas.id"))
    bankas = relationship("Bankas", back_populates="saskaitos")


if __name__ == "__main__":
    Base.metadata.create_all(engine)