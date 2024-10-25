import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.user_schema import UserInput, UserResponse, UserPasswordInput
from services.user_service import UserService

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/", status_code=201, response_model=UserResponse)
def create_user(data: UserInput, session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.create(data)

@router.patch("/{_id}/password", status_code=200, response_model=UserResponse)
def update_password(_id: uuid.UUID, data: UserPasswordInput, session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.update_password(_id, data)