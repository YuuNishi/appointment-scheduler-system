from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.address_schema import AddressInput, AddressResponse
from services.address_service import AddressService
from services.patient_service import PatientService

router = APIRouter(prefix="/address", tags=["address"])

@router.put("/{_id}", status_code=200, response_model=AddressResponse)
def update(_id:int, data: AddressInput, session: Session=Depends(get_db)):
    _service = AddressService(session)
    return _service.update(_id, data)

@router.delete("/{_id}", status_code=200, response_model=AddressResponse)
def delete(_id:int, session: Session = Depends(get_db)):
    _service = AddressService(session)
    return _service.delete(_id)