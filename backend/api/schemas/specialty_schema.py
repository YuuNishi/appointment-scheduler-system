from pydantic import BaseModel, Field

class SpecialtyInput(BaseModel):
  description: str = Field(min_length=1, max_length=50)

class SpecialtyResponse(BaseModel):
  id: int
  description: str