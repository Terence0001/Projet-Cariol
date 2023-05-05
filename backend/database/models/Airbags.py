from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

try:
    from database import Base
except:
    from ..database import Base


class Airbags(Base):
    __tablename__ = 'airbags'
    id = Column(Integer, primary_key=True)
    nb_airbag = Column(Integer)
