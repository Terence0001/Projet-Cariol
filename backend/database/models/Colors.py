from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String

try:
    from database import Base
except:
    from ..database import Base


class Colors(Base):
    __tablename__ = 'colors'

    id = Column(Integer, autoincrement=True, primary_key=True)
    color = Column(String)
