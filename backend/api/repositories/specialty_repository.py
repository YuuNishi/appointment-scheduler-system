from sqlalchemy.orm import Session
from models.specialty import Specialty
from schemas.specialty_schema import SpecialtyResponse

class SpecialtyRepository:
    def __init__(self, session: Session):
      self.session = session
    
    def create(self, specialty: Specialty):
      specialty = Specialty(**specialty.model_dump(exclude_none=True))
      self.session.add(specialty)
      self.session.commit()
      self.session.refresh(specialty)
      return SpecialtyResponse(**specialty.__dict__)
        
    def get_all(self):
        specialties= self.session.query(Specialty).filter_by()
        return specialties

    def get_by_description(self, _description: str):
        return self.session.query(Specialty).filter_by(description=_description).first()