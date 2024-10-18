from fastapi import APIRouter
from routers import patient
from routers import address
from routers import secretary

router = APIRouter(prefix="/api")

router.include_router(patient.router)
router.include_router(address.router)
router.include_router(secretary.router)
