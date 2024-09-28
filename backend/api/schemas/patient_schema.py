from datetime import date
from pydantic import BaseModel, Field
from schemas.person_schema import PersonInput, PersonResponse
class PatientInput(PersonInput):
    gender: int
    address: str
    birth_date: date
class PatientResponse(PersonResponse):
    id: int
    gender: int
    