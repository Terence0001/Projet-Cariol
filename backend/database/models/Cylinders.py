from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, Float
from sqlalchemy_serializer import SerializerMixin

try:
    from database import Base
except:
    from ..database import Base


class Cylinders(Base, SerializerMixin):
    __tablename__ = 'cylinders'

    id = Column(Integer, primary_key=True)
    cylinders = Column(Float)
