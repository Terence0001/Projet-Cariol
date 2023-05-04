from hug.middleware import CORSMiddleware
import hug

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api, allow_origins=['*'])) # allow_origins à restreindre pour le déploiement


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