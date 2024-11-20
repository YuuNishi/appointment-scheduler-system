from fastapi import APIRouter
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.token_schema import TokenResponse, TokenInput, KeepAliveTokenInput
from services.token_service import TokenService
from fastapi import Depends

router = APIRouter(prefix="/tokens", tags=["token"])

@router.post("/", status_code=201, response_model=TokenResponse)
def create_token(data: TokenInput, session: Session = Depends(get_db)):
    _service = TokenService(session)
    return _service.create(data)

@router.post("/keep-alive", status_code=201, response_model=TokenResponse)
def keep_alive(data: KeepAliveTokenInput, session: Session = Depends(get_db)):
    _service = TokenService(session)
    return _service.keep_alive(data)