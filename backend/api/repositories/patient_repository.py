from models.patient import Patient
from sqlalchemy.orm import Session
from schemas.patient_schema import PatientInput, PatientResponse

from models.person import Person


class PatientRepository:
    def __init__(self, session: Session):
        self.session = session
    def create(self, patient: Patient)-> PatientResponse:
        patient = Patient(**patient.model_dump(exclude_none=True))
        self.session.add(patient)
        self.session.commit()
        self.session.refresh(patient)
        return PatientResponse(**patient.__dict__)
    def get_all(self):
        patients= self.session.query(Patient).all()
        return patients