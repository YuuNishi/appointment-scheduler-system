from pydantic import BaseModel, EmailStr, Field

from models.enums import UserAvatarEnum
from utils.pattern import USERNAME_PATTERN

class UserInput(BaseModel):
    email: EmailStr = Field(max_length=100)
    username: str = Field(min_length=8, max_length=20, pattern=USERNAME_PATTERN)
    password: str = Field(min_length=8, max_length=30)

class UsernameInput(BaseModel):
    username: str = Field(min_length=8, max_length=20, pattern=USERNAME_PATTERN)

class UserAvatarInput(BaseModel):
    avatar: UserAvatarEnum

class UserPasswordInput(BaseModel):
    oldPassword: str = Field(min_length=8, max_length=30)
    newPassword: str = Field(min_length=8, max_length=30)

class UserResponse(BaseModel):
    username: str
    avatar: UserAvatarEnum