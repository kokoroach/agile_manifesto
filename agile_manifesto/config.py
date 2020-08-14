import os
from pathlib import Path

_path = Path(__file__).parent.absolute()

DB_DIR = os.path.join(_path, 'db')
DB_NAME = 'agile_manifesto.db'
DB_ENGINE = 'sqlite:///{}'.format(os.path.join(DB_DIR, DB_NAME))
