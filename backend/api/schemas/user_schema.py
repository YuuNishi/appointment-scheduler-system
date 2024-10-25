import uuid

from pydantic import BaseModel, EmailStr, Field

class UserInput(BaseModel):
    email: EmailStr = Field(max_length=100)
    username: str = Field(min_length=10, max_length=100)
    password: str = Field(min_length=15, max_length=30)

class UserPasswordInput(BaseModel):
    password: str = Field(min_length=15, max_length=30)

class UserResponse(BaseModel):
    username: str