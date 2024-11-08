from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.doctor_schema import DoctorResponse
from services.doctor_service import DoctorService

router = APIRouter(prefix="/doctors", tags=["doctor"])

@router.get("", status_code=200, response_model=List[DoctorResponse])
def get_all(session: Session = Depends(get_db)):
    _service = DoctorService(session)
    return _service.get_all()