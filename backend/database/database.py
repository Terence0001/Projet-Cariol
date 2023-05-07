from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

try:
    from getConfig import getConfig
except:
    from .getConfig import getConfig


''' Create engine and session communicate with database '''
engine = create_engine('postgresql://' + getConfig('user') + ':' + getConfig(
    'password') + '@localhost/' + getConfig('database') + '', echo=True)
session = sessionmaker(bind=engine)


Base = declarative_base()
