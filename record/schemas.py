# Pydantic is a Python library for data modeling/parsing that has efficient 
# error handling and a custom validation mechanism. 
# As of today, Pydantic is used mostly in the FastAPI framework for 
# parsing requests and responses because Pydantic has built-in support 
# for JSON encoding and decoding.
from pydantic import BaseModel

class Record(BaseModel):
    title: str
    destination: str
    start_date: str
    end_date: str
    description: str

class Traveler(BaseModel):
    name:str
    email:str