import time
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
# import json
import logging
import os
# import pickle
import numpy as np
import pandas as pd
import joblib

import azureml.automl.core
from azureml.automl.core.shared import logging_utilities, log_server
from azureml.telemetry import INSTRUMENTATION_KEY

from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType
from inference_schema.parameter_types.standard_py_parameter_type import StandardPythonParameterType


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
    drive_wheels = appendDefaultValue(
        'drive_wheels', 'Drive Wheel', drive_wheels)

    gear_box = session.query(GearBoxType).all()
    gear_box = appendDefaultValue('gears_type', 'Boîte de vitesse', gear_box)

    models = session.query(Model).all()
    models = appendDefaultValue('model', 'Modèles', models)

    manufacturers = session.query(Manufacturer).all()
    manufacturers = appendDefaultValue(
        'manufacturers', 'Marque', manufacturers)

    engines_volume = session.query(EngineVolume).all()
    engines_volume = appendDefaultValue(
        'volume', 'Volume moteur', engines_volume)

    fuels_type = session.query(FuelType).all()
    fuels_type = appendDefaultValue('fuel', 'Carburant', fuels_type)

    return {
        "engines_volume": engines_volume,
        "drive_wheels":  drive_wheels,
        "manufacturers": manufacturers,
        "categories": categories,
        "gears_type":  gear_box,
        "cylinders": cylinders,
        "colors":    colors,
        "airbags": airbags,
        "models": models,
        "doors": doors,
        "fuels_type": fuels_type,
    }


@hug.post('/api/prediction')
def prediction(body):
    print(body)
    time.sleep(1)
    return 'Le prix de la voiture vaut aujourd\'hui'


@hug.post('/api/car/prediction')
def prediction_with_local_data():
    data_sample = PandasParameterType(pd.DataFrame({"Manufacturer": pd.Series(["CHEVROLET"], dtype="object"), "Model": pd.Series(["Equinox"], dtype="object"), "Prod. year": pd.Series(["2000-1-1"], dtype="datetime64[ns]"), "Category": pd.Series(["Jeep"], dtype="object"), "Leather interior": pd.Series([False], dtype="bool"), "Fuel type": pd.Series(["Petrol"], dtype="object"), "Engine volume": pd.Series([0.0], dtype="float64"), "Mileage": pd.Series(
        [0], dtype="int64"), "Cylinders": pd.Series([0.0], dtype="float64"), "Gear box type": pd.Series(["example_value"], dtype="object"), "Drive wheels": pd.Series(["example_value"], dtype="object"), "Doors": pd.Series([0], dtype="int64"), "Wheel": pd.Series([False], dtype="bool"), "Color": pd.Series(["example_value"], dtype="object"), "Airbags": pd.Series([0], dtype="int64"), "Turbo": pd.Series([False], dtype="bool")}))
    input_sample = StandardPythonParameterType({'data': data_sample})

    result_sample = NumpyParameterType(np.array([0]))
    output_sample = StandardPythonParameterType({'Results': result_sample})
    sample_global_parameters = StandardPythonParameterType(1.0)

    try:
        log_server.enable_telemetry(INSTRUMENTATION_KEY)
        log_server.set_verbosity('INFO')
        logger = logging.getLogger('azureml.automl.core.scoring_script_v2')
    except:
        pass

    def init():
        global model
        # This name is model.id of model that we want to deploy deserialize the model file back
        # into a sklearn model
        model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')
        path = os.path.normpath(model_path)
        path_split = path.split(os.sep)
        log_server.update_custom_dimensions(
            {'model_name': path_split[-3], 'model_version': path_split[-2]})
        try:
            logger.info("Loading model from path.")
            model = joblib.load(model_path)
            logger.info("Loading successful.")
        except Exception as e:
            logging_utilities.log_traceback(e, logger)
            raise

    @input_schema('Inputs', input_sample)
    @input_schema('GlobalParameters', sample_global_parameters, convert_to_provided_type=False)
    @output_schema(output_sample)
    def run(Inputs, GlobalParameters=1.0):
        data = Inputs['data']
        result = model.predict(data)
        return {'Results': result.tolist()}
