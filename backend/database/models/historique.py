from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean


try:
    from database import Base
except:
    from ..database import Base


class Historique(Base):
    __tablename__ = 'historique'

    id = Column(autoincrement=True, primary_key=True)
    ProdYear = Column(Integer)
    LeatherInterior = Column(Boolean)
    MileAge = Column(Integer)
    column = mapped_column(ForeignKey('Engine_volume.id'))
    column = mapped_column(ForeignKey('Airbags.id'))
    column = mapped_column(ForeignKey('Categories.id'))
    column = mapped_column(ForeignKey('Colors.id'))
    column = mapped_column(ForeignKey('Cylinders.id'))
    column = mapped_column(ForeignKey('Doors.id'))
    column = mapped_column(ForeignKey('DriveWheel.id'))
    column = mapped_column(ForeignKey('EngineVolume.id'))
    column = mapped_column(ForeignKey('GearBoxType.id'))
    column = mapped_column(ForeignKey('Manufacturer.id'))
    column = mapped_column(ForeignKey('Model.id'))
