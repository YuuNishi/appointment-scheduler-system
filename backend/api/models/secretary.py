from sqlalchemy import Column, ForeignKey, Date
from sqlalchemy.orm import relationship
from models.person import Person

class Secretary(Person):
    __tablename__ = 'secretary'

    id = Column(ForeignKey('person.id'), primary_key=True,index=True)
    hiring_date = Column(Date)
    
    person = relationship('Person')

    __mapper_args__ = {
        'polymorphic_identity': 'secretary'
    }