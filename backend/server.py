from marshmallow import Schema, fields
import time
from hug.middleware import CORSMiddleware
import hug
from database.database import session
from database.Serializers import AirbagsObject, AirbagsSchema, CategoriesObject, CategoriesSchema, ColorsObject, ColorsSchema
from database.Serializers import CylindersObject, CylindersSchema, DoorsObject, DoorsSchema, DriveWheelObject, DriveWheelSchema
from database.Serializers import EngineVolumeObject, EngineVolumeSchema, FuelTypeObject, FuelTypeSchema, ManufacturerObject, ManufacturerSchema
from database.Serializers import WheelPositionObject, WheelPositionSchema, GearBoxTypeObject, GearBoxTypeSchema, HistoriqueObject, HistoriqueSchema
api = hug.API(__name__)
# allow_origins à restreindre pour le déploiement
api.http.add_middleware(CORSMiddleware(api, allow_origins=['*']))


@hug.get('/api/load-filters')
def loadFilters(body):
    return {
        "colors": [
            {"id": 0, "color": 'Couleur'},
            {"id": 1, "color": 'rouge'},
            {"id": 2, "color": 'bleu'},
            {"id": 3, "color": 'vert'}
        ],

        "cylinders":    [
            {"id": 0, "nb_cylinder": "Nb cylindres"},
            {"id": 1, "nb_cylinder": 6.0},
            {"id": 2, "nb_cylinder": 7.0},
            {"id": 3, "nb_cylinder": 8.0}

        ],
        "airbags":      [
            {"id": 0, 'nb_airbag': 'Nb airbagues'},
            {"id": 1, 'nb_airbag': 1},
        ],

        "doors":        [
            {"id": 0, 'nb_door': 'Nb portes'},
            {"id": 1, 'nb_door': 1},
            {"id": 2, 'nb_door': 2},


        ],

        "categories":   [
            {"id": 0, 'categorie': 'Categorie'},
            {"id": 1, 'categorie': 'Jeep'},
        ],

        "drive_wheels":   [
            {"id": 0, 'type': 'Drive Wheel'},
            {"id": 1, 'type': '...'},
        ],

        "gears_type":  [
            {"id": 0, 'type': 'Gear Box Type'},
            {"id": 1, 'type': 'Automatique'},
        ],

        "models":        [
            {"id": 0, "model": 'Modèles'},
            {"id": 1, "model": 'x9'}

        ],

        "manufacturers": [
            {"id": 0, "name": 'Constructeur'},
            {"id": 1, "name": 'Toyota'}

        ],

        "engines_volume": [
            {"id": 0, "engine_volume": 'Volume moteur'},
            {"id": 1, "engine_volume": 6.0}


        ],

        "fuels_type": [
            {"id": 0, "fuel": 'Type de carburant'}

        ],
    }


@hug.get('/api/airbags')
def get_airbags():
    my_object = AirbagsObject()
    my_schema = AirbagsSchema()
    serialized_obj = my_schema.dump(my_object)
    return serialized_obj


@hug.get('/api/categories')
def get_categories():
    my_object = CategoriesObject()
    my_schema = CategoriesSchema()
    serialized_obj = my_schema.dump(my_object)
    return serialized_obj


@hug.get('/api/colors')
def get_colors():
    my_object = ColorsObject()
    my_schema = ColorsSchema()
    serialized_obj = my_schema.dump(my_object)
    return serialized_obj


@hug.get('/api/cylinders')
def get_cylinders():
    my_object = CylindersObject()
    my_schema = CylindersSchema()
    serialized_obj = my_schema.dump(my_object)
    return serialized_obj


@hug.get('/api/doors')
def get_doors():
    my_object = DoorsObject()
    my_schema = DoorsSchema()
    serialized_obj = my_schema.dump(my_object)
    return serialized_obj


@hug.get('/api/driveWheel')
def get_drive_wheel():
    my_object = DriveWheelObject()
    my_schema = DriveWheelSchema()
    serialized_obj = my_schema.dump(my_object)
    return serialized_obj


@hug.get('/api/EngineVolume')
def get_engine_volume():
    my_object = EngineVolumeObject()
    my_schema = EngineVolumeSchema()
    serialized_obj = my_schema.dump(my_object)
    return serialized_obj


@hug.get('/api/FuelType')
def get_fuel_type():
    my_object = FuelTypeObject()
    my_schema = FuelTypeSchema()
    serialized_obj = my_schema.dump(my_object)
    return serialized_obj


@hug.get('/api/model')
def get_model():
    my_object = FuelTypeObject()
    my_schema = FuelTypeSchema()
    serialized_obj = my_schema.dump(my_object)
    return serialized_obj


@hug.get('/api/manufacturer')
def get_manufacturer():
    my_object = ManufacturerObject()
    my_schema = ManufacturerSchema()
    serialized_obj = my_schema.dump(my_object)
    return serialized_obj


@hug.get('/api/wheelPosition')
def get_wheel_position():
    my_object = WheelPositionObject()
    my_schema = WheelPositionSchema()
    serialized_obj = my_schema.dump(my_object)
    return serialized_obj


@hug.get('/api/gearBoxType')
def get_gear_box_type():
    my_object = GearBoxTypeObject()
    my_schema = GearBoxTypeSchema()
    serialized_obj = my_schema.dump(my_object)
    return serialized_obj


@hug.get('/api/historique')
def get_historique():
    my_object = HistoriqueObject()
    my_schema = HistoriqueSchema()
    serialized_obj = my_schema.dump(my_object)
    return serialized_obj

# @hug.get('/api/testSerializer')
# def TestSerializer(body):
#     # return 'Hello'
#     query = session.query(Airbags)
#     serializer = AirbagsSerializer
#     result = serializer(query)
#     return result


@hug.post('/api/prediction')
def prediction(body):
    print(body)
    time.sleep(1)
    return 'Le prix de la voiture vaut aujourd\'hui'
