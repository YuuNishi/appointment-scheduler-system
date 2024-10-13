from models.address import Address
from sqlalchemy.orm import Session
from schemas.address_schema import AddressInput, AddressResponse

class AddressRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, address: Address)-> AddressResponse:
        address = AddressResponse(**address.model_dump(exclude_none=True))
        self.session.add(address)
        self.session.commit()
        self.session.refresh(address)
        return AddressRepository(**address.__dict__)

    def get_by_id(self, _id: int):
        return self.session.query(Address).filter_by(id=_id).first()

    def exists_by_id(self, _id: id):
        address=self.session.query(Address).filter_by(id=_id).first()
        return bool(address)

    def update(self, data: AddressInput, address: Address):
        address.cep = data.cep
        address.street = data.street
        address.city = data.city
        address.federal_unit = data.federal_unit
        address.number = data.number
        address.neighborhood = data.neighborhood
        self.session.commit()
        self.session.refresh(address)
        return AddressResponse(**address.__dict__)

    def delete(self, address: Address):
        self.session.delete(address)
        self.session.commit()
        return AddressResponse(**address.__dict__)