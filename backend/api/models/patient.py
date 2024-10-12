from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from models.person import Person

class Patient(Person):
    __tablename__ = 'patient'

    id = Column(ForeignKey('person.id'), primary_key=True,index=True)
    address_id = Column(ForeignKey('address.id'))

    person = relationship('Person', foreign_keys=[id])
    address = relationship('Address', foreign_keys=[address_id])

    __mapper_args__ = {
        'polymorphic_identity': 'patient'
    }