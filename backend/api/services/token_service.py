import bcrypt
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository
from schemas.token_schema import TokenInput, TokenResponse, KeepAliveTokenInput
from utils.token_gen import TokenUtils

class TokenService:
    def __init__(self, session: Session):
        self.repository= session
        self.user_repository = UserRepository(session)

    def create(self, data: TokenInput):
        user = self.user_repository.get_by_email(data.email)
        
        if bool(user) and bcrypt.checkpw(data.password.encode('utf-8'), user.password):
            token = TokenUtils.generate_token(user)
        else:
            raise HTTPException(status_code=404, detail='E-mail e/ou senha incorretos')

        return TokenResponse(token=token, username=user.username)

    def keep_alive(self, data: KeepAliveTokenInput):
        credentials = HTTPAuthorizationCredentials(scheme="", credentials=data.token)
        decoded_token = TokenUtils.check_token(credentials)

        user = self.user_repository.get_by_email(decoded_token.email)

        if bool(user):
            token = TokenUtils.generate_token(user)
        else:
            raise HTTPException(status_code=401, detail='Token inválido')

        return TokenResponse(token=token, username=user.username)