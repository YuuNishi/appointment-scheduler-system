from sqlalchemy import Column, Integer, String
from database.database import Base

class Specialty(Base):
    __tablename__ = 'specialty'

    id = Column(Integer, primary_key=True, autoincrement=True,index=True)
    description = Column(String(50), nullable=False)