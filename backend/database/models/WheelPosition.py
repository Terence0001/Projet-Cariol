from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, Boolean

try:
    from database import Base
except:
    from ..database import Base


class WheelPosition(Base):
    __tablename__ = 'wheel'
    id = Column(Integer, autoincrement=True, primary_key=True)
    wheel_pos = Column(Boolean)
