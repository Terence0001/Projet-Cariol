from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_serializer import SerializerMixin

try:
    from database import Base
except:
    from ..database import Base


class GearBoxType(Base, SerializerMixin):
    __tablename__ = 'gear_box_type'

    id = Column(Integer, primary_key=True)
    gearbox = Column(String)
