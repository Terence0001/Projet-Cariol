from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

try:
    from database import Base
except:
    from ..database import Base

class Cylinders(Base):
    __tablename__ = 'cylinders'

    id = Column(autoincrement=True, primary_key=True)
    NbCylinders = Column(Integer)
