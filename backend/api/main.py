from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from routers.api import router

from utils.init_db import create_tables
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
<<<<<<< HEAD
    "http://localhost:8001",
    "http://localhost:5173",
=======
    "http://localhost:5173"
>>>>>>> 1fcd9fb92db8f772f6c654a4e74394e4fcc68292
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
async def on_startup():
    create_tables()
app.include_router(router)
