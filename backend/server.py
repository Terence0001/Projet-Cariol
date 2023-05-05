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
        "colors":       ['rouge'],
        "cylinders":    [6.0],
        "airbags":      [1],
        "doors":        [1, 2, 3, 4, 5],
        "categories":   ['jeep'],
        "driveWheel":   ['front'],
        "gearBoxType":  ['automatic'],
        "model":        ['prius'],
        "manufacturer": ['toyota'],
        "engineVolume": [1.8],
        "fuelType":     ["hybrided"],
    }

# Fuck sa marche pas


@hug.get('/api/testSerializer')
def TestSerializer(body):
    query = AirbagsSerializer.all()
    serializer = query.to_dict()
