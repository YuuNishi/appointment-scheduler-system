import jwt
from datetime import datetime, UTC
from cachetools import TTLCache
from models.user import User
from config import settings
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

token_cache = TTLCache(maxsize=100, ttl=3600)

class TokenUtils:

    @staticmethod
    def generate_token(user: User):
        payload = {
            'email': user.email,
            'createdDate': datetime.now(UTC).isoformat(),
        }

        token = jwt.encode(payload, settings.token_secret, algorithm='HS256')

        token_cache[token] = user.id

        return token

    @staticmethod
    def check_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
        token = credentials.credentials

        try:
            userid = token_cache.get(token)

            if userid is None:
                raise HTTPException(status_code=401, detail='Token não encontrado')

            token_cache[token] = userid
            return userid

        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Token inválido')