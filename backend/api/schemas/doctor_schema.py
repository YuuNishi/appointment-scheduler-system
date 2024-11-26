from pydantic import BaseModel, Field
from typing import Optional

class DoctorInput(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    speciality_id: int

class DoctorResponse(BaseModel):
    id: int
    name: str
    specialty: Optional[str] = None