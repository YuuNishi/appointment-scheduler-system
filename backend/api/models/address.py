from sqlalchemy import String, CHAR, Column, Integer
from database.database import Base

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    cep = Column(CHAR(8), nullable=False)
    street = Column(String(100), nullable=False)
    neighborhood = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    federal_unit = Column(CHAR(2), nullable=False)
    number = Column(Integer, nullable=False)