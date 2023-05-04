from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

try:
    from database import Base
except:
    from ..database import Base


class Colors(Base):
    __tablename__ = 'colors'

    id = Column(Integer, autoincrement=True, primary_key=True)
    colors = Column(String)
    formatedCode = Column(Integer)
