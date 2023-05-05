from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean
from database.models import Airbags


class AirbagsSerializer(Airbags, SerializerMixin, type):
    id = Column(Integer, autoincrement=True, primary_key=True)
    NbAirbags = Column(Integer)


class CategoriesSerializer(SerializerMixin):
    __tablename__ = 'categories'
    id = Column(Integer, autoincrement=True, primary_key=True)
    categorie_name = Column(String)
    code = Column(Integer)
    formatedCode = Column(Integer)


class ColorsSerializer(SerializerMixin):
    __tablename__ = 'colors'
    id = Column(Integer, autoincrement=True, primary_key=True)
    colors = Column(String)
    formatedCode = Column(Integer)


class CylindersSerializer(SerializerMixin):
    __tablename__ = 'cylinders'
    id = Column(Integer, autoincrement=True, primary_key=True)
    NbCylinders = Column(Float)


class DoorsSerializer(SerializerMixin):
    __tablename__ = 'doors'
    id = Column(Integer, autoincrement=True, primary_key=True)
    NbDoors = Column(Integer)


class DriveWheelSerializer(SerializerMixin):
    __tablename__ = 'drive_wheel'
    id = Column(Integer, autoincrement=True, primary_key=True)
    type = Column(String)


class EngineVolumeSerializer(SerializerMixin):
    __tablename__ = 'engine_volume'
    id = Column(Integer, autoincrement=True, primary_key=True)
    turbo = Column(Boolean)
    EngineVolume = Column(Float)


class GearBoxTypeSerializer(SerializerMixin):
    __tablename__ = 'gear_box_type'
    id = Column(Integer, autoincrement=True, primary_key=True)
    type = Column(String)


class ManufacturerSerializer(SerializerMixin):
    __tablename__ = 'manufacturer'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
