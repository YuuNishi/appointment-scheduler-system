from fastapi import APIRouter
from routers import patient

router = APIRouter(prefix="/api")

router.include_router(patient.router)