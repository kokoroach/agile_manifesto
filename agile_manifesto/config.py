import os
from utils.path import get_root_path

root = get_root_path()

DB_PATH = os.path.join(root, 'db', 'agile_manifesto.db')
DB_ENGINE = f'sqlite:///{DB_PATH}'
