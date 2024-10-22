from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.token_schema import TokenResponse, TokenInput
from services.token_service import TokenService

router = APIRouter(prefix="/token", tags=["token"])

@router.post("/", status_code=201, response_model=TokenResponse)
def create_token(data: TokenInput, session: Session = Depends(get_db)):
    _service = TokenService(session)
    return _service.create(data)