
from models import engine, Values, Principles
from utils.db import create_session


session = create_session(engine)


# GENERIC
def create_Data(tableObj, name):
    row = tableObj(name=name)
    session.add(row)


def commit():
    session.commit()


# Principles
def create_Value(name):
    return create_Data(Values, name)


# Values
def create_Principle(name):
    return create_Data(Principles, name)
