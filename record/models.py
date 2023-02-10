from sqlalchemy import Column, Integer, String
from .database import Base

# Define all the table and their fields in the database
# It extends the Base of the database
class Record(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    destination = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    description = Column(String)  

class Traveler(Base):
    __tablename__ = 'travelers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String) 