# FastAPI is a Python framework and set of tools that enables developers to use a 
# REST interface to call commonly used functions to implement applications. 
# It is accessed through a REST API to call common building blocks for an app. 
from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

# Create/migrate all the models/tables in the database whenever we are running the server 
models.Base.metadata.create_all(engine) 

# Use the SessionLocal to get the db, and close the db and its data connection after everthing is done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
# CRUD operations for TRAVEL RECORD

# Create a new record, return a status code 201 if record creating succeed
@app.post('/record', status_code=status.HTTP_201_CREATED)
# Convert the session into pydantic model with the get_db
def create_record(request: schemas.Record, db: Session = Depends(get_db)): 
    new_record = models.Record(title=request.title,
                                destination=request.destination,
                                start_date=request.start_date,
                                end_date=request.end_date,
                                description=request.description)
    db.add(new_record)
    # Commit the change request to database, otherwise the database will not be updated
    db.commit()
    db.refresh(new_record)
    if not new_record:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Record creating failed")
    return new_record

# Delete a record with given id
@app.delete('/record/{id}', status_code=status.HTTP_200_OK)
def delete_record(id, db: Session = Depends(get_db)):
    record = db.query(models.Record).filter(models.Record.id == id)

    # Check if the record is available, and raise execption if needed
    if not record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Record with the id {id} is not abailable")

    record.delete(synchronize_session=False)
    # Commit the change request to database, otherwise the database will not be updated
    db.commit()
    return f'Record with the id {id} is deleted'

# Update a record with given id
@app.put('/record/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_one_record(id, request: schemas.Record, db: Session = Depends(get_db)):
    record = db.query(models.Record).filter(models.Record.id == id)

    # Check if the record is available, and raise execption if needed
    if not record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Record with the id {id} is not abailable")

    record.update(request.dict())
    db.commit() 
    return f'Record with the id {id} is updated' 

# Get a list of records 
@app.get('/record', status_code=status.HTTP_200_OK)
def get_list_of_record(db: Session = Depends(get_db)):
    records = db.query(models.Record).all()

    # Check if the records are available, and raise execption if needed
    if not records:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No record currently available in the database")
    return records

# Get a specific record with given id
# Return a status code 200 if getting a record succeed, otherwise return 404, i.e., Not Found
@app.get('/record/{id}', status_code=status.HTTP_200_OK)
def get_one_record(id, db: Session = Depends(get_db)):
    record = db.query(models.Record).filter(models.Record.id == id).first()

    # Check if the record is available, and raise execption if needed
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Record with the id {id} is not abailable")
    return record

# CRUD operations for TRAVELER

# Create a new traveler, return a status code 201 if traveler creating succeed
@app.post('/traveler', status_code=status.HTTP_201_CREATED)
def create_traveler(request: schemas.Traveler, db: Session = Depends(get_db)):
    new_traveler = models.Traveler(name=request.name, email=request.email)
    db.add(new_traveler)
    # Commit the change request to database, otherwise the database will not be updated
    db.commit()
    db.refresh(new_traveler)
    if not new_traveler:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Traveler creating failed")
    return new_traveler


# Delete a traveler with given id
@app.delete('/traveler/{id}', status_code=status.HTTP_200_OK)
def delete_traveler(id, db: Session = Depends(get_db)):
    traveler = db.query(models.Traveler).filter(models.Traveler.id == id)

    # Check if the traveler is available, and raise execption if needed
    if not traveler.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Traveler with the id {id} is not abailable")

    traveler.delete(synchronize_session=False)
    # Commit the change request to database, otherwise the database will not be updated
    db.commit()
    return f'Traveler with the id {id} is deleted'

# Update a traveler with given id
@app.put('/traveler/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_one_traveler(id, request: schemas.Traveler, db: Session = Depends(get_db)):
    traveler = db.query(models.Traveler).filter(models.Traveler.id == id)

    # Check if the traveler is available, and raise execption if needed
    if not traveler.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Traveler with the id {id} is not abailable")

    traveler.update(request.dict())
    db.commit() 
    return f'Traveler with the id {id} is updated' 

# Get a list of travelers 
@app.get('/traveler', status_code=status.HTTP_200_OK)
def get_list_of_traveler(db: Session = Depends(get_db)):
    travelers = db.query(models.Traveler).all()

    # Check if the travelers are available, and raise execption if needed
    if not travelers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No traveler currently available in the database")
    return travelers

# Get a specific traveler with given id
# Return a status code 200 if getting a traveler succeed, otherwise return 404, i.e., Not Found
@app.get('/traveler/{id}', status_code=status.HTTP_200_OK)
def get_one_traveler(id, db: Session = Depends(get_db)):
    traveler = db.query(models.Traveler).filter(models.Traveler.id == id).first()

    # Check if the traveler is available, and raise execption if needed
    if not traveler:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Traveler with the id {id} is not abailable")
    return traveler
