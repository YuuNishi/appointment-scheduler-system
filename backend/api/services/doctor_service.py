from http.client import HTTPException
from sqlalchemy.orm import Session
from repositories.doctor_repository import DoctorRepository
from schemas.doctor_schema import DoctorInput, DoctorResponse

class DoctorService:
    def __init__(self, session: Session):
        self.repository= session
        self.doctor_repository = DoctorRepository(session)
        
    def create(self, data: DoctorInput):
        doctor = self.doctor_repository.create(data)
        return DoctorResponse(**doctor.model_dump(exclude_none=True))

    def delete(self, _id: int):
        doctor = self.doctor_repository.get_by_id(_id)

        if doctor is None:
            raise HTTPException(status_code=404, detail='Médico não encontrado')

        return self.doctor_repository.delete(doctor)
        
    def get_all(self):
        doctors = self.doctor_repository.get_all()

        return [
            DoctorResponse(
                id=doctor.id,
                name=doctor.name,
                specialty=doctor.speciality.description
            )
            for doctor in doctors
        ]