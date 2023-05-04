from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

try:
    from database import Base
except:
    from ..database import Base


class Model(Base):
    __tablename__ = 'model'

    id = Column(autoincrement=True, primary_key=True)
    ModelName = Column(String)
