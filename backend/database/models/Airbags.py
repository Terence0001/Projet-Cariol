from sqlalchemy import Column, Integer
from sqlalchemy_serializer import SerializerMixin
try:
    from database import Base
except:
    from ..database import Base


class Airbags(Base, SerializerMixin):
    __tablename__ = 'airbags'
    id = Column(Integer, primary_key=True)
    airbags = Column(Integer)
