from sqlalchemy import Column, Integer, String,Date,SmallInteger
from database.database import Base

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True,index=True)
    name = Column(String,nullable=False)
    status = Column(SmallInteger, nullable=False)
    gender = Column(SmallInteger,nullable=False)
    birth_date = Column(Date,nullable=False)
    cpf = Column(String, nullable=False)
    created_at = Column(Date)
    updated_at = Column(Date)
    type= Column(String, default='patient')

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': 'type'
    }