import os
from model import materialize_schema
from config import DB_DIR


def load_data():
    pass


def setup_db():
    if not os.path.exists(DB_DIR):
        os.mkdir(DB_DIR)
    materialize_schema()
    load_data()
