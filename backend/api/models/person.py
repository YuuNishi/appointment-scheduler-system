from sqlalchemy import Column, Integer, String,Date,SmallInteger
from datetime import datetime
from sqlalchemy.orm import relationship
from database.database import Base

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True,index=True)
    name = Column(String,nullable=False)
    gender = Column(SmallInteger,nullable=False)
    birth_date = Column(Date,nullable=False)
    created_at = Column(Date, default=datetime.now())
    updated_at = Column(Date, default=datetime.now())
    user = Column(String,nullable=False)
    password = Column(String,nullable=False)
    type= Column(String, default='patient')

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': 'type'
    }