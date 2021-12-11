from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from loguru import logger
from fastapi import HTTPException, status

from app.db.tables.cars import CarModel
from app.models.scheme.car import CreateCar, GetCar


class CarRepository:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    @logger.catch(reraise=True)
    async def create(self, car: CreateCar) -> CarModel:
        car = car.dict()
        new_car = CarModel(**car)
        self.db_session.add(new_car)
        await self.db_session.commit()
        return new_car

    @logger.catch()
    async def get_all(self) -> list[CarModel]:

        query = await self.db_session.execute(select(CarModel))

        return query.scalars().all()

    @logger.catch(reraise=True)
    async def get_by_id(self, car_id: int) -> GetCar:

        stmt = select(CarModel).where(CarModel.id == car_id)

        result = await self.db_session.execute(stmt)
        car = result.scalar()
        if car is None:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
        return car

    @logger.catch(reraise=True)
    async def car_update(self, car: GetCar) -> dict[str, str]:
        car_dict = car.dict()
        car_id = car_dict.pop('id', None)
        stmt = select(CarModel).where(CarModel.id == car_id)
        check_car = await self.db_session.execute(stmt)
        if not check_car.scalar():
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

        stmt = update(CarModel).where(CarModel.id == car_id).values(
            **car_dict).returning(CarModel)
        stmt.execution_options(synchronize_session="fetch")
        result = await self.db_session.execute(stmt)
        await self.db_session.commit()
        if result.scalar():
            return {"message": "success"}
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @logger.catch(reraise=True)
    async def delete_car(self, car_id: int) -> dict[str, str]:
        stmt = delete(CarModel).where(CarModel.id == car_id).returning(CarModel)
        stmt.execution_options(synchronize_session="fetch")
        result = await self.db_session.execute(stmt)
        await self.db_session.commit()
        if result.scalar():
            return {"message": "success"}
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
