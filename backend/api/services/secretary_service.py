from fastapi import HTTPException
from sqlalchemy.orm import Session
from repositories.secretary_repository import SercretaryRepository
from schemas.secretary_schema import SecretaryInput, SecretaryResponse

class Secretary_Service:
    def __init__(self, session: Session):
        self.repository = session
        self.secretary_repository = SercretaryRepository(session)
    def get_all(self):
        return self.secretary_repository.get_all()
    def create(self, secretary: SecretaryInput):
        secretary = self.secretary_repository.create(secretary)
        return SecretaryResponse(**secretary.model_dump(exclude_none=True))
    def update(self,_id:int, data: SecretaryInput):
        if not self.secretary_repository.exists_by_id(_id):
            raise HTTPException(status_code=404, detail='Atendente não encontrado')
        secretary = self.secretary_repository.get_by_id(_id)
        return self.secretary_repository.update(data, secretary)
    def delete(self,_id: int):
        if not self.secretary_repository.exists_by_id(_id):
            raise HTTPException(status_code=404, detail='Atendente não encontrado')
        secretary = self.secretary_repository.get_by_id(_id)
        return self.secretary_repository.delete(secretary)
