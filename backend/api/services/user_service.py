import uuid

import bcrypt
from fastapi import HTTPException

from sqlalchemy.orm import Session

from repositories.user_repository import UserRepository
from schemas.user_schema import UserInput, UserResponse, UserPasswordInput, UsernameInput, UserAvatarInput


class UserService:
    def __init__(self, session: Session):
        self.repository= session
        self.user_repository = UserRepository(session)

    def create(self, user: UserInput):
        if self.user_repository.user_exists(user.email, user.username):
            raise HTTPException(status_code=409, detail='Usuário já existente')

        user = self.user_repository.create(user)
        return UserResponse(**user.model_dump(exclude_none=True))

    def get_user_information(self, _id: uuid.UUID):
        user = self.user_repository.get_by_id(_id)
        
        if user is None:
            raise HTTPException(status_code=404, detail='Usuário não encontrado')

        return UserResponse(username=user.username, avatar=user.avatar)

    def update_password(self, _id: uuid.UUID, data: UserPasswordInput):
        user = self.user_repository.get_by_id(_id)

        if bool(user) and bcrypt.checkpw(data.oldPassword.encode('utf-8'), user.password):
            user = self.user_repository.update_password(user, data.newPassword)
        else:
            raise HTTPException(status_code=404, detail='Usuário não encontrado')

        return UserResponse(**user.model_dump(exclude_none=True))

    def update_username(self, _id: uuid.UUID, data: UsernameInput):
        user = self.user_repository.get_by_id(_id)

        if bool(user):
            if bool(self.user_repository.username_exists(data.username) == False):
                user = self.user_repository.update_username(user, data.username)
            else:
                raise HTTPException(status_code=409, detail='Usuário já existente')
        else:
            raise HTTPException(status_code=404, detail='Usuário não encontrado')

        return UserResponse(**user.model_dump(exclude_none=True))

    def update_avatar(self, _id: uuid.UUID, data: UserAvatarInput):
        user = self.user_repository.get_by_id(_id)

        if bool(user):
            user = self.user_repository.update_avatar(user, data.avatar)
        else:
            raise HTTPException(status_code=404, detail='Usuário não encontrado')

        return UserResponse(**user.model_dump(exclude_none=True))