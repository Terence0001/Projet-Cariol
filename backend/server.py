from hug.middleware import CORSMiddleware
import hug
from database.database import session
from database.models import Airbags
from database.Serializers import AirbagsSerializer


api = hug.API(__name__)
# allow_origins à restreindre pour le déploiement
api.http.add_middleware(CORSMiddleware(api, allow_origins=['*']))


@hug.get('/api/load-filters')
def loadFilters(body):
    return {
        "colors":[
            {"id": 0, "color": 'Couleur'},
            {"id": 1, "color": 'rouge'},
            {"id": 2, "color": 'bleu'},
            {"id": 3, "color": 'vert'}
        ],

        "cylinders":    [
            {"id": 1, "nb_cylinder": "Nb cylindres"},
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
        
        "driveWheel":   [
            {"id": 0, 'type': 'Drive Wheel'},
            {"id": 1, 'type': '...'},
        ],
        
        "gearBoxType":  [
            {"id": 0, 'type': 'Gear Box Type'},
            {"id": 1, 'type': 'Automatique'},
        ],
        
        "model":        [
            {"id": 0, "model": 'Modèles'},
            {"id": 1, "model": 'x9'}
        
        ],

        "manufacturer": [
            {"id": 0, "name": 'Constructeur'},
            {"id": 1, "name": 'Toyota'}

        ],
        
        "engineVolume": [
            {"id": 0, "engine_volume": 'Volume moteur'},
            {"id": 1, "engine_volume": 6.0}


        ],

        "fuelType": [
            {"id": 0, "fuel": 'Type de carburant'}

        ],
    }

# Fuck sa marche pas


@hug.get('/api/testSerializer')
def TestSerializer(body):
    query = AirbagsSerializer.all()
    serializer = query.to_dict()
