from fastapi import APIRouter
<<<<<<< HEAD
from routers import patient
from routers import address
from routers import secretary
=======
from routers import patient, address
>>>>>>> 72ae8aeb67361b3b73c1f2bdccbaf0638e688ba1

router = APIRouter(prefix="/api")

router.include_router(patient.router)
<<<<<<< HEAD
router.include_router(address.router)
router.include_router(secretary.router)
=======
router.include_router(address.router)
>>>>>>> 72ae8aeb67361b3b73c1f2bdccbaf0638e688ba1
