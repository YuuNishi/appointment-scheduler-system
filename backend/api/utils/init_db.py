from database.database import engine
from models.address import Address
from models.person import Person
from models.patient import Patient
from models.secretary import Secretary
from models.specialty import Specialty
from models.doctor import Doctor
from models.appointment import Appointment
from models.user import User

def create_tables():
    Address.metadata.create_all(bind=engine)
    Person.metadata.create_all(bind=engine)
    Patient.metadata.create_all(bind=engine)
    Secretary.metadata.create_all(bind=engine)
    Specialty.metadata.create_all(bind=engine)
    Doctor.metadata.create_all(bind=engine)
    Specialty.metadata.create_all(bind=engine)
    Appointment.metadata.create_all(bind=engine)
    User.metadata.create_all(bind=engine)