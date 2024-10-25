from fastapi import HTTPException

from sqlalchemy.orm import Session

from repositories.user_repository import UserRepository
from schemas.user_schema import UserInput, UserResponse, UserPasswordInput


class UserService:
    def __init__(self, session: Session):
        self.repository= session
        self.user_repository = UserRepository(session)

    def create(self, user: UserInput):
        if self.user_repository.user_exists(user.email, user.username):
            raise HTTPException(status_code=409, detail='Usuário já existente')

        user = self.user_repository.create(user)
        return UserResponse(**user.model_dump(exclude_none=True))

    def update_password(self, _id: int, data: UserPasswordInput):
        user = self.user_repository.get_by_id(_id)

        if bool(user):
            user = self.user_repository.update_password(user, data.password)
        else:
            raise HTTPException(status_code=404, detail='Usuário não encontrado')

        return UserResponse(**user.model_dump(exclude_none=True))