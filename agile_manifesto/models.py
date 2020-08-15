from config import DB_ENGINE

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(DB_ENGINE, echo=True)
Base = declarative_base()


class Values(Base):
    __tablename__ = "values"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Principles(Base):
    __tablename__ = "principles"

    id = Column(Integer, primary_key=True)
    name = Column(String)
