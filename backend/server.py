from hug.middleware import CORSMiddleware
import hug
from database.database import session
from database.models.Colors import Colors
from database.models.Cylinders import Cylinders
from database.models.Categories import Categories 
from database.models.Doors import Doors 
from database.models.Airbags import Airbags
from database.models.DriveWheel import DriveWheel
from database.models.GearBoxType import GearBoxType
from database.models.Model import Model
from database.models.Manufacturer import Manufacturer
from database.models.EngineVolume import EngineVolume
from database.models.FuelType import FuelType


# from database.Serializers import AirbagsSerializer


api = hug.API(__name__)
# allow_origins à restreindre pour le déploiement
api.http.add_middleware(CORSMiddleware(api, allow_origins=['*']))

''' Ajout une valeur avant toutes les autres dans la list,
    la valeur ajouter et une valeur par défaut pour l'élément sélect
    { id: 0, 'categorie': 'Catégorie'}
'''
def appendDefaultValue(featureName, featureValue, rows):
    featureJson = [{'id': 0, featureName: featureValue}]
    for row in rows:
        featureJson.append(row.to_dict())
    return featureJson

@hug.get('/api/load-filters')
def loadFilters(body):
    colors = session.query(Colors).all()
    colors = appendDefaultValue('color', 'Couleur', colors)

    cylinders = session.query(Cylinders).all()
    cylinders = appendDefaultValue('cylinders', 'Cylinder', cylinders) 
    
    categories = session.query(Categories).all()
    categories = appendDefaultValue('categorie', 'Categorie', categories) 
    
    doors = session.query(Doors).all()
    doors = appendDefaultValue('doors', 'Doors', doors) 

    airbags = session.query(Airbags).all()
    airbags = appendDefaultValue('airbags', 'Airbags', airbags)

    drive_wheels = session.query(DriveWheel).all()
    drive_wheels = appendDefaultValue('drive_wheels', 'Drive Wheel', drive_wheels)

    gear_box = session.query(GearBoxType).all()
    gear_box = appendDefaultValue('gears_type', 'Boîte de vitesse', gear_box)

    models = session.query(Model).all()
    models = appendDefaultValue('model', 'Modèles', models)

    manufacturers = session.query(Manufacturer).all()
    manufacturers = appendDefaultValue('manufacturers', 'Marque', manufacturers)
    
    engines_volume = session.query(EngineVolume).all()
    engines_volume = appendDefaultValue('volume', 'Volume moteur', engines_volume)

    fuels_type = session.query(FuelType).all()
    fuels_type = appendDefaultValue('fuel', 'Carburant', fuels_type)

    return {
        "engines_volume": engines_volume,
        "drive_wheels":  drive_wheels,
        "manufacturers":manufacturers,
        "categories": categories,
        "gears_type":  gear_box,
        "cylinders": cylinders,
        "colors":    colors,
        "airbags":airbags,
        "models": models,
        "doors": doors,
        "fuels_type": fuels_type,
    }

import time
@hug.post('/api/prediction')
def prediction(body):
    print(body)
    time.sleep(1)
    return 'Le prix de la voiture vaut aujourd\'hui'