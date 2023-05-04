from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

try:
    from database import Base
except:
    from ..database import Base


class Manufacturer(Base):
    __tablename__ = 'manufacturer'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)