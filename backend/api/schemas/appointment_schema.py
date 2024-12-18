from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import date, time

from models.enums import AppointmentTypeEnum, PaidEnum

class AppointmentInput(BaseModel):
    patient_id: int
    doctor_ids: List[int]
    title: str = Field(min_length=10, max_length=100)
    date: date
    start_time: time
    finish_time: time
    type: AppointmentTypeEnum

class AppointmentUpdateInput(BaseModel):
    patient_id: int
    doctor_ids: List[int]
    title: str = Field(min_length=10, max_length=100)
    date: date
    start_time: time
    finish_time: time
    type: AppointmentTypeEnum
    paid: PaidEnum
    
class AppointmentByRangeInput(BaseModel):
    start_date: date
    end_date: date
    criteria: Optional[str] = Field(max_length=100)
    
class AppointmentResponse(BaseModel):
    id: int
    
class AppointmentByRangeResponse(BaseModel):
    id: int
    title: str
    date: date
    start_time: time
    finish_time: time
    paid: PaidEnum

class AppointmentByIdResponse(BaseModel):
    title: str
    patient_id: int
    doctor_ids: List[int]
    type: AppointmentTypeEnum
    date: date
    start_time: time
    duration: int
    paid: PaidEnum
    status: int