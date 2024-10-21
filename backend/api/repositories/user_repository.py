import bcrypt
from models.address import Address
from sqlalchemy.orm import Session
from models.user import User
from schemas.address_schema import AddressInput, AddressResponse
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