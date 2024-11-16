from http.client import HTTPException

from sqlalchemy.orm import Session
from repositories.appointment_repository import AppointmentRepository
from schemas.appointment_schema import AppointmentInput, AppointmentResponse, AppointmentByRangeInput, \
    AppointmentByRangeResponse, AppointmentUpdateInput


class AppointmentService:
    def __init__(self, session: Session):
        self.repository= session
        self.appointment_repository = AppointmentRepository(session)
    
    def create(self, data: AppointmentInput):
        appointment = self.appointment_repository.create(data, data.doctor_ids)
        return AppointmentResponse(**appointment.model_dump(exclude_none=True))

    def update(self, _id: int, data: AppointmentUpdateInput):
        appointment = self.appointment_repository.get_by_id(_id)

        if not bool(appointment):
            raise HTTPException(status_code=404, detail='Consulta não encontrada')

        return self.appointment_repository.update(data, appointment)
    
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