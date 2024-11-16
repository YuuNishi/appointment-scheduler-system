from pydantic import BaseModel

class DoctorInput(BaseModel):
    name: str
    speciality_id: int

class DoctorResponse(BaseModel):
    id: int
    name: str