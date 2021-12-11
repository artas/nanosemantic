import pytest
import json
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status

from app.db.repositories.cars import CarRepository
from app.models.scheme.car import CreateCar

PAYLOAD = {
    "name": "granta",
    "car_type": "sedan",
    "year_publication": "2018-12-10",
    "mark": "LADA",
    "mileage": 0,
    "horsepower": 300
}


@pytest.mark.asyncio
async def test_create_car(
        async_client: AsyncClient
) -> None:
    response = await async_client.post('/cars/create', json=PAYLOAD)

    print(response)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.asyncio
async def test_get_by_id(
        async_client: AsyncClient, db_session: AsyncSession
) -> None:
    payload = CreateCar.parse_raw(json.dumps(PAYLOAD))
    car_repository = CarRepository(db_session)
    car = await car_repository.create(payload)
    print(car.id)
    response = await async_client.get(f"/cars/{car.id}")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_all(
        async_client: AsyncClient, db_session: AsyncSession
) -> None:
    payload = CreateCar.parse_raw(json.dumps(PAYLOAD))
    car_repository = CarRepository(db_session)
    await car_repository.create(payload)
    response = await async_client.get("/cars/all")
    assert response.status_code == 200
    assert response.json() == [{
        "name": "granta",
        "car_type": "sedan",
        "year_publication": "2018-12-10",
        "mark": "LADA",
        "mileage": 0,
        "horsepower": 300,
        "id": 1
    }]


@pytest.mark.asyncio
async def test_update(
        async_client: AsyncClient, db_session: AsyncSession
) -> None:
    payload = CreateCar.parse_raw(json.dumps(PAYLOAD))
    car_repository = CarRepository(db_session)
    car = await car_repository.create(payload)
    car.name = 'tets'
    response = await async_client.put('/cars/update',
                                      json={"id": 1, "name": "test",
                                            "car_type": "sedan",
                                            "year_publication": "2018-12-10",
                                            "mark": "LADA",
                                            "mileage": 0,
                                            "horsepower": 300})
    assert response.status_code == 200
    assert response.json() == {
        "message": "success"
    }


@pytest.mark.asyncio
async def test_delete(
        async_client: AsyncClient, db_session: AsyncSession
) -> None:
    payload = CreateCar.parse_raw(json.dumps(PAYLOAD))
    car_repository = CarRepository(db_session)
    car = await car_repository.create(payload)
    response = await async_client.delete(f'/cars/delete?car_id={car.id}')
    assert response.status_code == 200
    assert response.json() == {
        "message": "success"
    }
