from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.db import get_db
from app.db.repositories.cars import CarRepository
from app.models.scheme.car import GetCar, CreateCar

router = APIRouter()


@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(db: AsyncSession = Depends(get_db)):
    car_repository = CarRepository(db)
    return await car_repository.get_all()


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_by_id(id: int, db: AsyncSession = Depends(get_db)):
    car_repository = CarRepository(db)
    return await car_repository.get_by_id(id)


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_car(payload: CreateCar, db: AsyncSession = Depends(get_db)):
    car_repository = CarRepository(db)
    return await car_repository.create(payload)


@router.put('/update')
async def update(payload: GetCar, db: AsyncSession = Depends(get_db)):
    car_repository = CarRepository(db)
    return await car_repository.car_update(payload)


@router.delete('/delete')
async def delete(car_id: int, db: AsyncSession = Depends(get_db)):
    car_repository = CarRepository(db)
    return await car_repository.delete_car(car_id)
