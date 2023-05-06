from marshmallow import Schema, fields
import time
from hug.middleware import CORSMiddleware
import hug
from database.database import session
from database.Serializers import AirbagsObject, AirbagsSchema


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
def get_my_object():
    my_object = AirbagsObject(1, 2)
    my_schema = AirbagsSchema()
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
