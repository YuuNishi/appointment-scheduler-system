from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import date, time

from models.enums import AppointmentTypeEnum, PaidEnum

class AppointmentInput(BaseModel):
    patient_id: int
    doctor_ids: List[int]
    created_by: str = Field(min_length=10, max_length=100)
    title: str = Field(min_length=10, max_length=100)
    date: date
    start_time: time
    finish_time: time
    type: AppointmentTypeEnum
    
class AppointmentByRangeInput(BaseModel):
    start_date: date
    end_date: date
    criteria: Optional[str] = Field(max_length=100)
    
class AppointmentCreateResponse(BaseModel):
    id: int
    
class AppointmentByRangeResponse(BaseModel):
    id: int
    title: str
    date: date
    start_time: time
    finish_time: time
    paid: PaidEnum