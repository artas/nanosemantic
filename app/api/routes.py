from fastapi import APIRouter
from app.api import cars

router = APIRouter()
router.include_router(cars.router, prefix="/cars")