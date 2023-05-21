from sqlalchemy import Column, Integer
from sqlalchemy_serializer import SerializerMixin

try:
    from database import Base
except:
    from ..database import Base


class Doors(Base, SerializerMixin):
    __tablename__ = 'doors'

    id = Column(Integer, primary_key=True)
    doors = Column(Integer)
