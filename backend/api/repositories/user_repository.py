import bcrypt
from sqlalchemy.orm import Session
from sqlalchemy import or_
from models.user import User
from schemas.user_schema import UserInput, UserResponse

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, data: UserInput) -> UserResponse:
        hashed_password = bcrypt.hashpw(data.password.encode('utf-8') , bcrypt.gensalt())
        
        user = User(**data.model_dump(exclude_none=True))
        user.password = hashed_password
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        
        return UserResponse(**user.__dict__)

    def get_by_email(self, email: str):
        return self.session.query(User).filter_by(email=email).first()

    def user_exists(self, email: str, username: str):
        return self.session.query(User).filter(or_(email == email, username == username)).first() is not None