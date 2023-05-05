from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String

try:
    from database import Base
except:
    from ..database import Base


class Model(Base):
    __tablename__ = 'model'

    id = Column(Integer, autoincrement=True, primary_key=True)
    model = Column(String)
