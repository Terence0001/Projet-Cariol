from database import engine

# from models.columns import Columns, Base
# from models.tasks   import Tasks,   Base

from models.Airbags import Airbags, Base
from models.Categories import Categories, Base
from models.Colors import Colors, Base
from models.Cylinders import Cylinders, Base
from models.Doors import Doors, Base
from models.DriveWheel import DriveWheel, Base
from models.EngineVolume import EngineVolume, Base
from models.GearBoxType import GearBoxType, Base
from models.Manufacturer import Manufacturer, Base
from models.Model import Model, Base
from models.Historique import Historique, Base


''' Create all table'''
# Base.metadata.create_all(engine)
