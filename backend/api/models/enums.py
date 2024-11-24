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

class UserAvatarEnum(enum.Enum):
    placeholder = 0
    assistant = 1
    female_doc = 2
    male_doc = 3