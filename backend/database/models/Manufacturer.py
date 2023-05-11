from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_serializer import SerializerMixin

try:
    from database import Base
except:
    from ..database import Base


class Manufacturer(Base, SerializerMixin):
    __tablename__ = 'manufacturer'

    id = Column(Integer, primary_key=True)
    name = Column(String)
