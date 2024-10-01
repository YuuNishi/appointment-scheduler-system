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
        patients= self.session.query(Patient).filter_by(status=1)
        return patients
    def get_by_id(self, _id: int):
        return self.session.query(Patient).filter_by(id=_id).first()
    def exists_by_id(self, _id: id):
        patient=self.session.query(Patient).filter_by(id=_id).first()
        return bool(patient)
    def update(self, data: PatientInput, patient: Patient):
        patient.name = data.name
        patient.cpf = data.cpf
        patient.address = data.address
        patient.birth_date = data.birth_date
        self.session.commit()
        self.session.refresh(patient)
        return PatientInput(**patient.__dict__)
    def delete(self, patient: Patient):
        patient.status = 0
        self.session.commit()
        self.session.refresh(patient)
        return PatientInput(**patient.__dict__)