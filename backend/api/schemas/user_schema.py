import uuid

from pydantic import BaseModel, EmailStr, Field

class UserInput(BaseModel):
    email: EmailStr = Field(max_length=100)
    username: str = Field(min_length=10, max_length=100)
    password: str = Field(min_length=8, max_length=30)

class UsernameInput(BaseModel):
    username: str = Field(min_length=10, max_length=100)

class UserPasswordInput(BaseModel):
    oldPassword: str = Field(min_length=8, max_length=30)
    newPassword: str = Field(min_length=8, max_length=30)

class UserInfoResponse(BaseModel):
    id: uuid.UUID
    username: str

class UserResponse(BaseModel):
    username: str