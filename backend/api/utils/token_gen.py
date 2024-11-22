import jwt

from datetime import datetime, timedelta, UTC

from models.user import User

from config import settings
from schemas.token_schema import TokenData

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

class TokenUtils:

    @staticmethod
    def generate_token(user: User):
        payload = {
            'id': str(user.id),
            'email': user.email,
            'exp': datetime.now(UTC) + timedelta(hours=1)
        }

        return jwt.encode(payload, settings.token_secret, algorithm='HS256')

    @staticmethod
    def check_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
        token = credentials.credentials

        try:
            payload = jwt.decode(token, settings.token_secret, algorithms=['HS256'])
            decoded_token = TokenData(**payload)
            if datetime.now(UTC) > decoded_token.exp:
                raise HTTPException(status_code=401, detail='Token expirado')

            return decoded_token

        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Token inválido')

    @staticmethod
    def decoded_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
        token = credentials.credentials

        try:
            payload = jwt.decode(token, settings.token_secret, algorithms=['HS256'])
            decoded_token = TokenData(**payload)

            return decoded_token

        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Token inválido')