from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.secretary_schema import SecretaryResponse, SecretaryInput
from services.secretary_service import Secretary_Service
from models.secretary import Secretary

router = APIRouter(prefix="/secretary", tags=["secretary"])

@router.post("/", status_code=201, response_model=SecretaryResponse)
def create_patient(dados: SecretaryInput, session: Session = Depends(get_db)):
    _service = Secretary_Service(session)
    return _service.create(dados)
@router.get("", status_code=200, response_model=List[SecretaryResponse])
def get_all(session: Session = Depends(get_db)):
    _service = Secretary_Service(session)
    return _service.get_all()
@router.put("/{_id}", status_code=200, response_model=SecretaryInput)
def update(_id:int, data: SecretaryInput, session: Session=Depends(get_db)):
    _service = Secretary_Service(session)
    return _service.update(_id, data)
@router.patch("/{_id}", status_code=200, response_model=SecretaryInput)
def delete(_id:int, session: Session = Depends(get_db)):
    _service = Secretary_Service(session)
    return _service.delete(_id)
