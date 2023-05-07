from datetime import date
from pprint import pprint
from typing import Any
from database.models.Airbags import Airbags
from marshmallow import Schema, fields


class CategoriesObject:
    def __call__(self, id, category_name):
        self.id = id
        self.category_name = category_name


class CategoriesSchema(Schema):
    id = fields.Int()
    category_name = fields.Str()


class AirbagsObject:
    def __call__(self, id, nb_airbag):
        self.id = id
        self.nb_airbag = nb_airbag


class AirbagsSchema(Schema):
    id = fields.Int()
    nb_airbag = fields.Int()


class ColorsObject:
    def __call__(self, id, color):
        self.id = id
        self.color = color


class ColorsSchema(Schema):
    id = fields.Int()
    color = fields.Str()


class CylindersObject:
    def __call__(self, id, nb_cylinder):
        self.id = id
        self.nb_cylinder = nb_cylinder


class CylindersSchema(Schema):
    id = fields.Int()
    nb_cylinder = fields.Float()


class DoorsObject:
    def __call__(self, id, nb_door):
        self.id = id
        self.nb_door = nb_door


class DoorsSchema(Schema):
    id = fields.Int()
    nb_door = fields.Int()


class DriveWheelObject:
    def __call__(self, id, dw_type):
        self.id = id
        self.dw_type = dw_type


class DriveWheelSchema(Schema):
    id = fields.Int()
    dw_type = fields.Str()


class EngineVolumeObject:
    def __call__(self, id, turbo, engine_volume):
        self.id = id
        self.turbo = turbo
        self.engine_volume = engine_volume


class EngineVolumeSchema(Schema):
    id = fields.Int()
    turbo = fields.Boolean()
    engine_volume = fields.Float()


class FuelTypeObject:
    def __call__(self, id, f_type):
        self.id = id
        self.f_type = f_type


class FuelTypeSchema(Schema):
    id = fields.Int()
    f_type = fields.Str()


class ModelObject:
    def __call__(self, id, model_name):
        self.id = id
        self.model_name = model_name


class ModelSchema(Schema):
    id = fields.Int()
    model_name = fields.Str()


class ManufacturerObject:
    def __call__(self, id, name):
        self.id = id
        self.name = name


class ManufacturerSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class WheelPositionObject:
    def __call__(self, id, wheel_pos):
        self.id = id
        self.wheel_pos = wheel_pos


class WheelPositionSchema(Schema):
    id = fields.Int()
    wheel_pos = fields.Boolean()


class GearBoxTypeObject:
    def __call__(self, id, gb_type):
        self.id = id
        self.gb_type = gb_type


class GearBoxTypeSchema(Schema):
    id = fields.Int()
    gb_type = fields.Str()


class HistoriqueObject:
    def __call__(self, id, ProdYear, LeatherInterior, MileAge):
        self.id = id
        self.ProdYear = ProdYear
        self.LeatherInterior = LeatherInterior
        self.MileAge = MileAge


class HistoriqueSchema(Schema):
    id = fields.Int()
    ProdYear = fields.Date()
    LeatherInterior = fields.Boolean()
    MileAge = fields.Int()

# #Test d'une autre méthode qui affiche des données bidons
# class AirbagsSchema(Schema):
#     id = fields.Int()
#     nb_airbag = fields.Int()

#     class Meta:
#         ordered = True


# class AirbagsSerializer:
#     @staticmethod
#     def serialize(airbags):
#         schema = AirbagsSchema()
#         return schema.dump(airbags)


# airbags = Airbags(id=1, nb_airbag=16)
# serializer = AirbagsSerializer()
# result = serializer.serialize(airbags)
# print('______________________________________________________')
# print(result)
# print('______________________________________________________')
