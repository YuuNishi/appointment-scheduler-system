from datetime import date
from typing import Optional
from models.enums import SexEnum
from schemas.person_schema import PersonInput, PersonResponse

class PatientInput(PersonInput):
    sex: SexEnum
    address_id: Optional[int] = None
    birth_date: date

class PatientResponse(PersonResponse):
    id: int
    sex: SexEnum