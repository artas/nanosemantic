from pydantic import BaseModel
from datetime import date
from app.db.tables.cars import CarModel


class BaseSchema(BaseModel):
    class Config(BaseModel.Config):
        orm_mode = True


class CreateCar(BaseModel):
    name: str
    car_type: str
    year_publication: date
    mark: str
    mileage: int
    horsepower: int

    class Meta:
        orm_model = CarModel


class GetCar(CreateCar):
    id: int
