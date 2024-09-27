from sqlalchemy import String, Column, Integer, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from models.person import Person
from database.database import Base
class Patient(Person):
    __tablename__ = ('patient')
    id = Column(Integer, ForeignKey('person.id'), primary_key=True,index=True)
    status = Column(SmallInteger, nullable=False)
    address = Column(String, nullable=False)
    #person= relationship("Person", back_populates="patients")
    __mapper_args__ = {
        'polymorphic_identity': 'patient'
    }