from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_serializer import SerializerMixin

try:
    from database import Base
except:
    from ..database import Base


class DriveWheel(Base, SerializerMixin):
    __tablename__ = 'drive_wheel'

    id = Column(Integer, primary_key=True)
    drivewheel = Column(String)
