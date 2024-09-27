from fastapi import HTTPException
from sqlalchemy.orm import Session
from repositories.patient_repository import PatientRepository
from schemas.patient_schema import PatientInput, PatientResponse


class PatientService:
    def __init__(self, session: Session):
        self.repository= session
        self.patient_repository = PatientRepository(session)
    def get_all(self):
        return self.patient_repository.get_all()
    def create(self, patient:PatientInput):
        patient = self.patient_repository.create(patient)
        return PatientResponse(**patient.model_dump(exclude_none=True))