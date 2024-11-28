from sqlalchemy import String, Column, Integer, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship
from database.database import Base
from models.doctor_appointment import doctor_appointment

class Doctor(Base):
    __tablename__ = 'doctor'
    
    id = Column(Integer, primary_key=True, autoincrement=True,index=True)
    name = Column(String(100), nullable=False)
    speciality_id = Column(Integer, ForeignKey('specialty.id'))
    status = Column(SmallInteger, default=0, nullable=False)

    speciality = relationship('Specialty')
    appointments = relationship('Appointment', secondary=doctor_appointment, back_populates='doctors')