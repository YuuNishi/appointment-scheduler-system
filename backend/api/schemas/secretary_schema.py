from datetime import date
from schemas.person_schema import PersonInput, PersonResponse

class SecretaryInput(PersonInput):
    hiring_date: date
class SecretaryResponse(PersonResponse):
    id: int