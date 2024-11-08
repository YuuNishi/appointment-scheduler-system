from sqlalchemy.orm import Session
from repositories.doctor_repository import DoctorRepository
from schemas.doctor_schema import DoctorResponse

class DoctorService:
    def __init__(self, session: Session):
        self.repository= session
        self.doctor_repository = DoctorRepository(session)
    def get_all(self):
        doctors = self.doctor_repository.get_all()
        return [
            DoctorResponse(
                id=doctor.id,
                name=doctor.name
            )
            for doctor in doctors
        ]