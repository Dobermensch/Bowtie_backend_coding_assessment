from fastapi import APIRouter
from app.api.routes.doctors import router as doctors_router

router = APIRouter()

router.include_router(doctors_router, prefix="/doctors", tags=["doctors"])
