from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
<<<<<<< HEAD
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///data/tevai_vaikai.db')
=======
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/tevai_vaikai_o2m.db')
>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
Base = declarative_base()


class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
<<<<<<< HEAD
    pavarde =Column(String)
=======
    pavarde = Column(String)
>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
    vaikai = relationship("Vaikas", back_populates="tevas")


class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
<<<<<<< HEAD
    pavarde =Column(String)
    mokymosi_istaiga = Column(String)
=======
    pavarde = Column(String)
    mokymo_istaiga = Column(String)
>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
    tevas_id = Column(Integer, ForeignKey("tevas.id"))
    tevas = relationship("Tevas", back_populates="vaikai")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
