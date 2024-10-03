from datetime import date

from pydantic import BaseModel, Field

class PersonInput(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    status: int
    gender: int
    birth_date: date
    cpf: str = Field(min_length=11 , max_length=11)


class PersonResponse(BaseModel):
    id: int
    name: str
    status: int
    gender:int
    birth_date: date
    cpf: str