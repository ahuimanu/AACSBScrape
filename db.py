
from sqlalchemy import create_engine

from models import Base, College

conn_string = 'sqlite:///foo.db'
engine = create_engine(conn_string)

def init_db():
    Base.metadata.create_all(engine)

