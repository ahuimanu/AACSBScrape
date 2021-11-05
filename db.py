
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base, College

conn_string = 'sqlite:///schools.db'
engine = create_engine(conn_string)

def init_db():
    Base.metadata.create_all(engine)

def get_record_from_school_text(school_text):
    lines = school_text.splitlines()
    print(f"lines length {len(lines)}")
    pass

def write_school(school):
    """ Schools is a list of School objects"""
    with Session(engine) as session:
        session.add(school)
        session.commit()
        
