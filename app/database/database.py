from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app import myConfig


db_string = myConfig.SQLALCHEMY_DATABASE_URI

db = create_engine(db_string, connect_args={'check_same_thread': False})
base = declarative_base()

Session = sessionmaker(db)
session = Session()
