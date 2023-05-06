from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String

try:
    from database import Base
except:
    from ..database import Base


class FuelType(Base):
    __tablename__ = 'fuel_type'
    id = Column(Integer, autoincrement=True, primary_key=True)
    f_type = Column(String)
