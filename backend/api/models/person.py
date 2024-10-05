from datetime import datetime
from sqlalchemy import Column, Enum, SmallInteger, Integer, String, CHAR, Date, DateTime
from database.database import Base
from models.enums import SexEnum

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, autoincrement=True,index=True)
    name = Column(String(100), nullable=False)
    status = Column(SmallInteger, default=0, nullable=False)
    sex = Column(Enum(SexEnum),nullable=False)
    birth_date = Column(Date,nullable=False)
    cpf = Column(CHAR(11), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime)
    type= Column(String, default='patient')

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': 'type'
    }