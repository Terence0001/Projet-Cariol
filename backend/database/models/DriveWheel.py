from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

try:
    from database import Base
except:
    from ..database import Base


class DriveWheel(Base):
    __tablename__ = 'drive_wheel'
    id = Column(Integer, autoincrement=True, primary_key=True)
    dw_type = Column(String)
