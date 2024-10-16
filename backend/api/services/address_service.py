
from sqlalchemy.orm import Session
from repositories.address_repository import AddressRepository
from schemas.address_schema import AddressInput, AddressResponse

class AddressService:
    def __init__(self, session: Session):
        self.repository= session
        self.address_repository = AddressRepository(session)
    def get_all(self):
        return self.address_repository.get_all()
    def create(self, address: AddressInput):
        address = self.address_repository.create(address)
        return AddressResponse(**address.model_dump(exclude_none=True))
        