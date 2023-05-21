from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin

try:
    from database import Base
except:
    from ..database import Base


class Model(Base, SerializerMixin):
    __tablename__ = 'model'

    id = Column(Integer, primary_key=True)
    model = Column(String)
