from sqlalchemy import String, Column, Integer, ForeignKey
from models.person import Person
class Patient(Person):
    __tablename__ = ('patient')
    id = Column(Integer, ForeignKey('person.id'), primary_key=True,index=True)
    address = Column(String, nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'patient'
    }