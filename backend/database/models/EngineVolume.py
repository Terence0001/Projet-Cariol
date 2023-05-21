from sqlalchemy import Column, Integer, Boolean, Float
from sqlalchemy_serializer import SerializerMixin

try:
    from database import Base
except:
    from ..database import Base


class EngineVolume(Base, SerializerMixin):
    __tablename__ = 'engine_volume'

    id = Column(Integer, primary_key=True)
    turbo = Column(Boolean)
    volume = Column(Float)
