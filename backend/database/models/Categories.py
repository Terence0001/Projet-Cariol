from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String

try:
    from database import Base
except:
    from ..database import Base


class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, autoincrement=True, primary_key=True)
    category_name = Column(String)
