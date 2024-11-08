from pydantic import BaseModel

class DoctorResponse(BaseModel):
    id: int
    name: str