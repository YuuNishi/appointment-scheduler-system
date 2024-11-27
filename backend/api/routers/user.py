import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.user_schema import UserInput, UserResponse, UserPasswordInput, UsernameInput, UserAvatarInput
from services.user_service import UserService
from utils.token_gen import TokenUtils

router = APIRouter(prefix="/users", tags=["user"])

@router.post("/", status_code=201, response_model=UserResponse)
def create_user(data: UserInput, session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.create(data)

@router.get("/user/info", status_code=200, response_model=UserResponse)
def get_user_information(userid: uuid.UUID = Depends(TokenUtils.check_token), session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.get_user_information(userid)

@router.patch("/change/password", status_code=200, response_model=UserResponse)
def update_password(data: UserPasswordInput, userid: uuid.UUID = Depends(TokenUtils.check_token), session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.update_password(userid, data)

@router.patch("/change/username", status_code=200, response_model=UserResponse)
def update_username(data: UsernameInput, userid: uuid.UUID = Depends(TokenUtils.check_token), session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.update_username(userid, data)

@router.patch("/change/avatar", status_code=200, response_model=UserResponse)
def update_avatar(data: UserAvatarInput, userid: uuid.UUID = Depends(TokenUtils.check_token), session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.update_avatar(userid, data)