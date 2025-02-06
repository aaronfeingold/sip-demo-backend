from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import pgvector.sqlalchemy

Base = declarative_base()


class Wine(Base):
    __tablename__ = "wines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    region = Column(String, nullable=False)
    varietal = Column(String, nullable=False)
    description = Column(String, nullable=True)
    spectator_score = Column(Float, nullable=True)
    vector = Column(pgvector.sqlalchemy.Vector(1536))  # OpenAI embedding size


class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cuisine = Column(String, nullable=True)
    description = Column(String, nullable=True)


class WinePairing(Base):
    __tablename__ = "wine_pairings"

    id = Column(Integer, primary_key=True, index=True)
    wine_id = Column(Integer, ForeignKey("wines.id"))
    food_id = Column(Integer, ForeignKey("foods.id"))

    wine = relationship("Wine")
    food = relationship("Food")
