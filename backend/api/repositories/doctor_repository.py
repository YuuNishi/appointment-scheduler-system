from models.doctor import Doctor
from sqlalchemy.orm import Session

from models.specialty import Specialty
from schemas.doctor_schema import DoctorResponse

class DoctorRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def create(self, doctor: Doctor):
        doctor = Doctor(**doctor.model_dump(exclude_none=True))
        self.session.add(doctor)
        self.session.commit()
        self.session.refresh(doctor)
        return DoctorResponse(**doctor.__dict__)

    def get_by_id(self, _id: int):
        return self.session.query(Doctor).filter_by(id=_id).first()

    def delete(self, doctor: Doctor):
        self.session.delete(doctor)
        self.session.commit()
        return DoctorResponse(**doctor.__dict__)
        
    def get_all(self):
        doctors= self.session.query(Doctor).join(Specialty, Specialty.id == Doctor.speciality_id).filter_by()
        return doctors