import os
from databases import Database
from sqlalchemy import create_engine, MetaData

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
DB_PATH = os.path.join(BASE_DIR, "test.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

database = Database(DATABASE_URL)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata = MetaData()