import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.token_schema import TokenData
from schemas.user_schema import UserInput, UserResponse, UserPasswordInput, UserInfoResponse, UsernameInput
from services.user_service import UserService
from utils.token_gen import TokenUtils

router = APIRouter(prefix="/users", tags=["user"])

@router.post("/", status_code=201, response_model=UserResponse)
def create_user(data: UserInput, session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.create(data)

@router.get("/user/info", status_code=200)
def get_user_information(credentials: TokenData = Depends(TokenUtils.decoded_token), session: Session = Depends(get_db)):
    print(credentials)

@router.patch("/{_id}/password", status_code=200, response_model=UserResponse)
def update_password(_id: uuid.UUID, data: UserPasswordInput, session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.update_password(_id, data)

@router.patch("/{_id}/username", status_code=200, response_model=UserResponse)
def update_username(_id: uuid.UUID, data: UsernameInput, session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.update_username(_id, data)