from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.user_schema import UserInput, UserResponse
from services.user_service import UserService

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/", status_code=201, response_model=UserResponse)
def create_user(data: UserInput, session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.create(data)