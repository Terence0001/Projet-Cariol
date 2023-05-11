from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin

try:
    from database import Base
except:
    from ..database import Base


class Colors(Base, SerializerMixin):
    __tablename__ = 'colors'

    id = Column(Integer,  primary_key=True)
    color = Column(String)
