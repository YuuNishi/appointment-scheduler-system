from fastapi import APIRouter
from routers import patient
from routers import address
from routers import secretary
from routers import user

router = APIRouter(prefix="/api")

router.include_router(patient.router)
router.include_router(address.router)
router.include_router(secretary.router)
router.include_router(user.router)
