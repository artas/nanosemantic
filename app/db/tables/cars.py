from sqlalchemy import Column, Integer, String, Date
from app.db.session import Base


class CarModel(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    car_type = Column(String, nullable=False)
    year_publication = Column(Date, nullable=False)
    mark = Column(String, nullable=False)
    mileage = Column(Integer, nullable=False)
    horsepower = Column(Integer, nullable=False)

