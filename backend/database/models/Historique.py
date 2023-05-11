from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy_serializer import SerializerMixin


try:
    from database import Base
except:
    from ..database import Base


class Historique(Base, SerializerMixin):
    __tablename__ = 'historique'

    id = Column(Integer, primary_key=True)
    ProdYear = Column(Date)
    MileAge  = Column(Integer)
    LeatherInterior = Column(Boolean)

    airbags   = relationship(ForeignKey('airbags.id'), backref='historique')
    categorie = relationship(ForeignKey('categories.id'), backref='historique')
    color     = relationship(ForeignKey('colors.id'), backref='historique')
    cylinder  = relationship(ForeignKey('cylinders.id'), backref='historique')
    doors     = relationship(ForeignKey('doors.id'), backref='historique')
    gearbox   = relationship(ForeignKey('gear_box_type.id'))
    model     = relationship(ForeignKey('model.id'), backref='historique')
    manufacturer  = relationship(ForeignKey('manufacturer.id'), backref='historique')
    drive_wheel   = relationship(ForeignKey('drive_wheel.id'), backref='historique')
    engine_volume = relationship(ForeignKey('engine_volume.id'), backref='historique')
