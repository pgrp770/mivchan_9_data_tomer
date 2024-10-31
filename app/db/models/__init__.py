from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .country import Country
from .city import City
from .mission import Missions
from .target_type import TargetTypes
from .target import Target