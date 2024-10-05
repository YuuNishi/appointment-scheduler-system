from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from models.person import Person

class Secretary(Person):
    __tablename__ = 'secretary'

    id = Column(ForeignKey('person.id'), primary_key=True,index=True)

    person = relationship('Person')

    __mapper_args__ = {
        'polymorphic_identity': 'secretary'
    }