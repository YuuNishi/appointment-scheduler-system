import uuid
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

class TokenInput(BaseModel):
    email: EmailStr = Field(max_length=100)
    password: str = Field(min_length=8, max_length=30)

class KeepAliveTokenInput(BaseModel):
    token: str

class TokenResponse(BaseModel):
    token: str
    username: str

class TokenData(BaseModel):
    id: uuid.UUID
    email: str
    exp: datetime