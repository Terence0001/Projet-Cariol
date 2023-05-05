from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, Float

try:
    from database import Base
except:
    from ..database import Base


class Cylinders(Base):
    __tablename__ = 'cylinders'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nb_cylinder = Column(Float)
