from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date


try:
    from database import Base
except:
    from ..database import Base


class Historique(Base):
    __tablename__ = 'historique'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ProdYear = Column(Date)
    LeatherInterior = Column(Boolean)
    MileAge = Column(Integer)
    column = mapped_column(ForeignKey('engine_volume.id'))
    column = mapped_column(ForeignKey('airbags.id'))
    column = mapped_column(ForeignKey('categories.id'))
    column = mapped_column(ForeignKey('colors.id'))
    column = mapped_column(ForeignKey('cylinders.id'))
    column = mapped_column(ForeignKey('doors.id'))
    column = mapped_column(ForeignKey('drive_wheel.id'))
    column = mapped_column(ForeignKey('gear_box_type.id'))
    column = mapped_column(ForeignKey('manufacturer.id'))
    column = mapped_column(ForeignKey('model.id'))
    column = mapped_column(ForeignKey('historique.id'))
