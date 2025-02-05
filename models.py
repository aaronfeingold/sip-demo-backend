from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from pgvector.sqlalchemy import Vector

Base = declarative_base()

class Wine(Base):
    __tablename__ = "wines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    region = Column(String)
    varietal = Column(String)
    description = Column(String)
    spectator_score = Column(Float)
    pairing_vector = Column(Vector(1536))  # Vector embedding for pairings
