from sqlalchemy import Column, Integer, String, Table, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

<<<<<<< HEAD
engine = create_engine('sqlite:///data/tevai_vaikai.m2m.db')
Base = declarative_base()

tevai_vaikai = Table('tevas_vaikas', Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("tevas_id", Integer, ForeignKey("tevas.id")),
    Column("vaikas_id", Integer, ForeignKey("vaikas.id"))
)

=======
engine = create_engine('sqlite:///data/tevai_vaikai_m2m.db')
Base = declarative_base()


tevai_vaikai = Table('tevas_vaikas', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('tevas_id', Integer, ForeignKey('tevas.id')),
    Column('vaikas_id', Integer, ForeignKey('vaikas.id'))
)


>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
<<<<<<< HEAD
    pavarde =Column(String)
    vaikai = relationship("Vaikas", secondary=tevai_vaikai, back_populates="tevai")

=======
    pavarde = Column(String)
    vaikai = relationship("Vaikas", secondary=tevai_vaikai, back_populates="tevai")


>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
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
    tevai = relationship("Tevas", secondary=tevai_vaikai, back_populates="vaikai")


if __name__ == "__main__":
<<<<<<< HEAD
    Base.metadata.create_all(engine)
=======
    Base.metadata.create_all(engine)
>>>>>>> fbfa35b09b8bfe035025677fef3adc5f63f404ee
