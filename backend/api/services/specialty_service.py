from sqlalchemy.orm import Session
from repositories.specialty_repository import SpecialtyRepository
from schemas.specialty_schema import SpecialtyInput, SpecialtyResponse

class SpecialtyService:
    def __init__(self, session: Session):
        self.repository= session
        self.specialty_repository = SpecialtyRepository(session)
        
    def create(self, data: SpecialtyInput):
        specialty = self.specialty_repository.create(data)
        return SpecialtyResponse(**specialty.model_dump(exclude_none=True))
        
    def get_all(self):
        specialties = self.specialty_repository.get_all()
        return [
            SpecialtyResponse(
                id=specialty.id,
                description=specialty.description
            )
            for specialty in specialties
        ]