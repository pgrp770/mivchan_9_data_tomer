from graphene import ObjectType, Int, String, Field

from app.db.database import session_maker
from app.db.models import Missions, City, TargetTypes
from app.gql.types.city_type import CityType
from app.gql.types.mission_type import MissionsType
from app.gql.types.targets_types_type import TargetTypesType


class TargetType(ObjectType):
    target_id = Int()

    target_industry = String()
    target_priority = Int()

    mission_id = Int()
    mission = Field(MissionsType)

    @staticmethod
    def resolve_mission(root, info):
        with session_maker() as session:
            session.query(Missions).filter(Missions.mission_id == root.mission_id).all()

    city_id = Int()
    city = Field(CityType)

    @staticmethod
    def resolve_city(root, info):
        with session_maker() as session:
            session.query(City).filter(City.city_id == root.city_id).all()

    target_type_id = Int()
    target_type = Field(TargetTypesType)

    @staticmethod
    def resolve_target_type(root, info):
        with session_maker() as session:
            session.query(TargetTypes).filter(TargetTypes.target_type_id == root.target_type_id).all()
