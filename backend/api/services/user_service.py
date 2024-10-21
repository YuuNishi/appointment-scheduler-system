from sqlalchemy.orm import Session

from repositories.user_repository import UserRepository
from schemas.user_schema import UserInput, UserResponse

class UserService:
    def __init__(self, session: Session):
        self.repository= session
        self.user_repository = UserRepository(session)

    def create(self, user: UserInput):
        user = self.user_repository.create(user)
        return UserResponse(**user.model_dump(exclude_none=True))