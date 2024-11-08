from sqlalchemy import or_
from sqlalchemy.orm import Session
from models.appointment import Appointment
from models.doctor import Doctor
from models.patient import Patient
from models.person import Person
from schemas.appointment_schema import AppointmentByRangeInput, AppointmentCreateResponse, AppointmentInput

class AppointmentRepository:
    def __init__(self, session: Session):
        self.session = session
        
    def create(self, data: AppointmentInput, doctor_ids: list[int])-> AppointmentCreateResponse:
        appointment = Appointment(**data.model_dump(exclude_none=True, exclude={"doctor_ids"}))
        
        doctors = self.session.query(Doctor).filter(Doctor.id.in_(doctor_ids)).all()
        appointment.doctors = doctors
        
        self.session.add(appointment)
        self.session.commit()
        self.session.refresh(appointment)
        return AppointmentCreateResponse(**appointment.__dict__)
    
    def get_by_range(self, data: AppointmentByRangeInput):
        haveCriteria = bool(data.criteria)
        
        if haveCriteria:
            search = f"%{data.criteria}%"
            print(search)
            return self.session.query(Appointment).\
                join(Patient, Appointment.patient_id == Patient.id).\
                filter(
                    Appointment.date >= data.start_date,
                    Appointment.date <= data.end_date,
                    or_(
                        Appointment.title.like(search), 
                        Patient.person.has(Person.name.like(search))  # Filtrando pelo nome usando a relação
                    )
                ).order_by(Appointment.date).all()
        else:
            return self.session.query(Appointment).filter(
                Appointment.date >= data.start_date,
                Appointment.date <= data.end_date
            ).order_by(Appointment.date).all()