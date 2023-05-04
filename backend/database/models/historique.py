from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

try:
    from database import Base
except:
    from ..database import Base
    
class Historique(Base):
    __tablename__ = 'historique'

    id       = Column(Integer, primary_key=True) 
    title    = Column(String)
    position = Column(Integer)
    desc     = Column(String)
    column   = mapped_column(ForeignKey('columns.id'))

