from fastapi import APIRouter, Depends
from routers import patient, address, secretary, user, token
from utils.token_gen import TokenUtils

router = APIRouter(prefix="/api")

PROTECTED = [Depends(TokenUtils.check_token)]

router.include_router(patient.router, dependencies = PROTECTED)
router.include_router(address.router, dependencies = PROTECTED)
router.include_router(secretary.router, dependencies = PROTECTED)
router.include_router(user.router)
router.include_router(token.router)