from database.database import engine
from models.person import Person
from models.patient import Patient

def create_tables():
    Person.metadata.create_all(bind=engine)
    Patient.metadata.create_all(bind=engine)