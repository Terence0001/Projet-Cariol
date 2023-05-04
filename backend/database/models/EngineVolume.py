from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

try:
    from database import Base
except:
    from ..database import Base


class EngineVolume(Base):
    __tablename__ = 'engine_volume'

    id = Column(autoincrement=True, primary_key=True)
    turbo = Column(Boolean)
    EngineVolume = Column(Integer)
