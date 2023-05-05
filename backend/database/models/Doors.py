from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

try:
    from database import Base
except:
    from ..database import Base


class Doors(Base):
    __tablename__ = 'doors'

    id = Column(Integer, autoincrement=True, primary_key=True)
    NbDoor = Column(Integer)
