# SQLAlchemy is a library that facilitates the communication between Python programs and databases. 
# Most of the times, this library is used as an Object Relational Mapper (ORM) tool that translates 
# Python classes to tables on relational databases and automatically converts function calls to SQL statements.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set the URL for the database
SQLALCHAMY_DATABASE_URL = 'sqlite:///./record/db'

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={
    "check_same_thread": False
})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()