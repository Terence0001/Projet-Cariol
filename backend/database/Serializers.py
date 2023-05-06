from datetime import date
from pprint import pprint
from database.models.Airbags import Airbags
from marshmallow import Schema, fields


class AirbagsObject:
    def __init__(self, id, nb_airbag):
        self.id = id
        self.nb_airbag = nb_airbag


class AirbagsSchema(Schema):
    id = fields.Integer()
    nb_airbag = fields.Integer()


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


class CategoriesSerializer(Schema):
    id = fields.Int()
    category_name = fields.Str()


class ColorsSerializer(Schema):
    id = fields.Int()
    color = fields.Str(unique=True)


class CylinderSerializer(Schema):
    id = fields.Int()
    nb_cylinder = fields.Int()


class DoorsSerializer(Schema):
    id = fields.Int()
    nb_door = fields.Int()


class DriveWhellSerializer(Schema):
    id = fields.Int()
    dw_type = fields.Str()


class EngineVolumeSerializer(Schema):
    id = fields.Int()
    turbo = fields.Boolean()
    engine_volume = fields.Float()


class fuelTypeSerializer(Schema):
    id = fields.Int()
    f_type = fields.Str()


class GearBoxTypeSerializer(Schema):
    id = fields.Int()
    gb_type = fields.Str()


class ManufacturerSerializer(Schema):
    id = fields.Int()
    name = fields.Str()


class ModelSerializer(Schema):
    id = fields.Int()
    model_name = fields.Str()


class WheelPositionSerializer(Schema):
    id = fields.Int()
    wheel_pos = fields.Boolean()
