from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.patient_schema import PatientResponse, PatientInput
from services.patient_service import PatientService

router = APIRouter(prefix="/patient", tags=["patient"])

@router.post("/", status_code=201, response_model=PatientResponse)
def create_patient(dados: PatientInput, session: Session = Depends(get_db)):
    _service = PatientService(session)
    return _service.create(dados)

@router.get("", status_code=200, response_model=List[PatientResponse])
def get_all(session: Session = Depends(get_db)):
    _service = PatientService(session)
    return _service.get_all()
@router.put("/{_id}", status_code=200, response_model=PatientInput)
def update(_id:int, data: PatientInput, session: Session=Depends(get_db)):
    _service = PatientService(session)
    return _service.update(_id, data)
@router.patch("/{_id}", status_code=200, response_model=PatientInput)
def delete(_id:int, session: Session = Depends(get_db)):
    _service = PatientService(session)
    return _service.delete(_id)