from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from database.database import get_db
<<<<<<< HEAD
from schemas.address_schema import AddressResponse, AddressInput
from services.address_service import AddressService

router = APIRouter(prefix="/address", tags=["address"])

@router.post("/", status_code=201, response_model=AddressResponse)
def create_address(dados: AddressInput, session: Session = Depends(get_db)):
    _service = AddressService(session)
    return _service.create(dados)

@router.get("", status_code=200, response_model=List[AddressResponse])
def get_all(session: Session = Depends(get_db)):
    _service = AddressService(session)
    return _service.get_all()
=======
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
>>>>>>> 72ae8aeb67361b3b73c1f2bdccbaf0638e688ba1
