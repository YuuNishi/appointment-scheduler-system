from datetime import date, datetime

from pydantic import BaseModel, Field

class PersonInput(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    gender: int
    birth_date: date
    user : str = Field(min_length=1, max_length=100)
    password : str = Field(min_length=1, max_length=16)


class PersonResponse(BaseModel):
    id: int
    name: str
    gender:int
    birth_date: date
