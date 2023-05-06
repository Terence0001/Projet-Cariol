from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

try:
    from database import Base
except:
    from ..database import Base


class GearBoxType(Base):
    __tablename__ = 'gear_box_type'

    id = Column(Integer, autoincrement=True, primary_key=True)
    gb_type = Column(String)
