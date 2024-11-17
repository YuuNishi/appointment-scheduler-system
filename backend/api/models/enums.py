import enum

class AppointmentTypeEnum(enum.Enum):
    routine_consultation = 0
    specialty_appointment = 1
    emergency_appointment = 2
    return_appointment = 3

class PaidEnum(enum.Enum):
    pending = 0
    paid = 1

class SexEnum(enum.Enum):
    male = 0
    female = 1