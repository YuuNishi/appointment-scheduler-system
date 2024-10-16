from pydantic import BaseModel, Field

class AddressInput(BaseModel):
    cep: str = Field(min_length=8, max_length=8)
    street: str = Field(max_length=100)
    neighborhood: str = Field(max_length=100)
    city: str = Field(max_length=100)
    federal_unit: str = Field(min_length=2, max_length=2)
    number: int

class AddressResponse(BaseModel):
    id: int
    street: str