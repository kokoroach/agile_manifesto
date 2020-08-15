import os
import registrar as reg

from config import DB_PATH
from utils.db import create_session, materialize_schema
from models import Base, engine, Values, Principles


def load_default_data():
    from setup.default_data import VALUES, PRINCIPLES
    for value in VALUES:
        reg.create_Value(value)
    for principle in PRINCIPLES:
        reg.create_Principle(principle)
    reg.commit()


def setup_db():
    if not os.path.exists(DB_PATH):
        if not os.path.exists(DB_DIR := os.path.dirname(DB_PATH)):
            os.mkdir(DB_DIR)
        materialize_schema(Base, engine)
        load_default_data()
