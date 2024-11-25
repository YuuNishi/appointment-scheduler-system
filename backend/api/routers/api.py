from fastapi import APIRouter, Depends
from routers import patient, address, secretary, user, token, appointment, doctor, specialty
from utils.token_gen import TokenUtils

router = APIRouter(prefix="/api")

PROTECTED = [Depends(TokenUtils.check_token)]

router.include_router(patient.router, dependencies = PROTECTED)
router.include_router(address.router, dependencies = PROTECTED)
router.include_router(secretary.router, dependencies = PROTECTED)
router.include_router(appointment.router, dependencies = PROTECTED)
router.include_router(user.router)
router.include_router(token.router)
router.include_router(doctor.router, dependencies = PROTECTED)
router.include_router(specialty.router, dependencies = PROTECTED)