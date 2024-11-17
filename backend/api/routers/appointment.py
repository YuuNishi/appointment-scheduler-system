from datetime import date
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.appointment_schema import AppointmentInput, AppointmentResponse, AppointmentByRangeInput, \
    AppointmentByRangeResponse, AppointmentUpdateInput, AppointmentByIdResponse
from services.appointment_service import AppointmentService

router = APIRouter(prefix="/appointments", tags=["appointment"])

@router.post("/", status_code=201, response_model=AppointmentResponse)
def create(data: AppointmentInput, session: Session = Depends(get_db)):
    _service = AppointmentService(session)
    return _service.create(data)

@router.put("/{_id}", status_code=200, response_model=AppointmentResponse)
def create(_id:int, data: AppointmentUpdateInput, session: Session = Depends(get_db)):
    _service = AppointmentService(session)
    return _service.update(_id, data)

@router.delete("/{_id}", status_code=200, response_model=AppointmentResponse)
def delete(_id:int, session: Session = Depends(get_db)):
    _service = AppointmentService(session)
    return _service.disable(_id)

@router.get("/range", status_code=200, response_model=List[AppointmentByRangeResponse])
def get_by_range(start_date: date, end_date: date, criteria: str | None = None, session: Session = Depends(get_db)):
    data = AppointmentByRangeInput(start_date=start_date, end_date=end_date, criteria=criteria)
    _service = AppointmentService(session)
    return _service.get_by_range(data)

@router.get("/{_id}", status_code=200, response_model=AppointmentByIdResponse)
def get_by_id(_id:int, session: Session = Depends(get_db)):
    _service = AppointmentService(session)
    return _service.get_by_id(_id)