from sqlalchemy import Column, ForeignKey, Table
from database.database import Base

doctor_appointment = Table(
  'doctor_appointment',
  Base.metadata,
  Column('doctor_id', ForeignKey('doctor.id'), primary_key=True),
  Column('appointment_id', ForeignKey('appointment.id'), primary_key=True)
)