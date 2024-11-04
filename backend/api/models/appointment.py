from datetime import datetime
from sqlalchemy import CheckConstraint, Column, Date, DateTime, Enum, ForeignKey, SmallInteger, Integer, String, Table, Time
from sqlalchemy.orm import relationship
from database.database import Base
from models.enums import PaidEnum, AppointmentTypeEnum
from models.doctor_appointment import doctor_appointment

class Appointment(Base):
    __tablename__ = 'appointment'
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    patient_id = Column(ForeignKey('patient.id'), nullable=False)
    created_by = Column(ForeignKey('user.username'), nullable=False)
    status = Column(SmallInteger, default=0, nullable=False)
    title = Column(String(100), nullable=False)
    date = Column(Date)
    start_time = Column(Time)
    finish_time = Column(Time)
    type = Column(Enum(AppointmentTypeEnum), nullable=False)
    paid = Column(Enum(PaidEnum), default=PaidEnum.pending, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

    patient = relationship('Patient', foreign_keys=[patient_id])
    user = relationship('User', foreign_keys=[created_by])
    doctors = relationship('Doctor', secondary=doctor_appointment, back_populates='appointments')

    CheckConstraint('start_time < finish_time', name='check_time_range')