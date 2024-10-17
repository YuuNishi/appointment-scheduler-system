from models.secretary import Secretary
from sqlalchemy.orm import Session
from schemas.secretary_schema import SecretaryInput, SecretaryResponse

class SercretaryRepository:
    def __init__(self, session: Session):
        self.session = session
    def create(self, secretary: Secretary) -> SecretaryResponse:
        secretary = Secretary(**secretary.model_dump(exclude_none=True))
        self.session.add(secretary)
        self.session.commit()
        self.session.refresh(secretary)
        return SecretaryResponse(**secretary.__dict__)
    def get_all(self):
        secretaries = self.session.query(Secretary).filter_by(status=1)
        return secretaries
    def get_by_id(self, _id: int):
        return self.session.query(Secretary).filter_by(id=_id).first()
    def exists_by_id(self, _id: id):
        secretary = self.session.query(Secretary).filter_by(id=_id).first()
        return bool(secretary)
    def update(self, data: SecretaryInput, secretary: Secretary):
        secretary.name = data.name
        secretary.cpf = data.cpf
        secretary.birth_date = data.birth_date
        secretary.sex = data.sex
        self.session.commit()
        self.session.refresh(secretary)
        return SecretaryInput(**secretary.__dict__)
    def delete(self, secretary: Secretary):
        secretary.status = 0
        self.session.commit()
        self.session.refresh(secretary)
        return SecretaryInput(**secretary.__dict__)