from sqlalchemy.orm import Session
from repositories.appointment_repository import AppointmentRepository
from schemas.appointment_schema import AppointmentInput, AppointmentCreateResponse, AppointmentByRangeInput, AppointmentByRangeResponse

class AppointmentService:
    def __init__(self, session: Session):
        self.repository= session
        self.appointment_repository = AppointmentRepository(session)
    
    def create(self, data: AppointmentInput):
        appointment = self.appointment_repository.create(data)
        return AppointmentCreateResponse(**appointment.model_dump(exclude_none=True))
    
    def get_by_range(self, data: AppointmentByRangeInput):
        appointments = self.appointment_repository.get_by_range(data)
        return [
            AppointmentByRangeResponse(
                id=appointment.id,
                title=appointment.title,
                date=appointment.date,
                start_time=appointment.start_time,
                finish_time=appointment.finish_time,
                paid=appointment.paid
            )
            for appointment in appointments
        ]