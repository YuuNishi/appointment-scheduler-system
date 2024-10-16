from sqlalchemy import Column, ForeignKey, Date
from models.person import Person

class Secretary(Person):
    __tablename__ = 'secretary'

    id = Column(ForeignKey('person.id'), primary_key=True,index=True)

    hiring_date = Column(Date)

    __mapper_args__ = {
        'polymorphic_identity': 'secretary'
    }