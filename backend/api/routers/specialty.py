from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.specialty_schema import SpecialtyResponse, SpecialtyInput
from services.specialty_service import SpecialtyService

router = APIRouter(prefix="/specialties", tags=["doctor"])

@router.get("", status_code=200, response_model=List[SpecialtyResponse])
def get_all(session: Session = Depends(get_db)):
    _service = SpecialtyService(session)
    return _service.get_all()

@router.post("/", status_code=201)
def create_specialty(data: SpecialtyInput, session: Session = Depends(get_db)):
    _service = SpecialtyService(session)
    return _service.create(data)