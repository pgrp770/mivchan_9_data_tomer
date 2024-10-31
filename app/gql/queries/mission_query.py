from graphene import ObjectType, Field, Int, List, Date, String

from app.gql.types.mission_type import MissionsType
from app.repository.mission_repository import get_mission_by_id, get_mission_between_dates, get_mission_by_country, \
    get_mission_by_target_industry, get_mission_by_target_type


class MissionQuery(ObjectType):
    mission_by_id = Field(MissionsType, mission_id=Int(required=True))

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        return get_mission_by_id(mission_id)

    mission_by_dates = List(MissionsType, start_date=Date(required=True), end_date=Date(required=True))

    @staticmethod
    def resolve_mission_by_dates(root, info, start_date, end_date):
        return get_mission_between_dates(start_date, end_date)

    mission_by_country = List(MissionsType, country=String(required=True))

    @staticmethod
    def resolve_mission_by_country(root, info, country):
        return get_mission_by_country(country)

    mission_by_target_industry = List(MissionsType, target_industry=String(required=True))

    @staticmethod
    def resolve_mission_by_target_industry(root, info, target_industry):
        return get_mission_by_target_industry(target_industry)

    mission_by_target_type = List(MissionsType, target_type=String(required=True))

    @staticmethod
    def resolve_mission_by_target_type(root, info, target_type):
        return get_mission_by_target_type(target_type)
