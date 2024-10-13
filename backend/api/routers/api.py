from fastapi import APIRouter
from routers import patient, address

router = APIRouter(prefix="/api")

router.include_router(patient.router)
router.include_router(address.router)