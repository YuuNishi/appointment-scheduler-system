from models.doctor import Doctor
from sqlalchemy.orm import Session

class DoctorRepository:
    def __init__(self, session: Session):
        self.session = session
    def get_all(self):
        doctors= self.session.query(Doctor).filter_by()
        return doctors