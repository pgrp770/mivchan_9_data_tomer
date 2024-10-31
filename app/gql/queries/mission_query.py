from graphene import ObjectType, Field, Int, List, Date, String

from app.db.database import session_maker
from app.db.models.city import City
from app.db.models.country import Country
from app.db.models.mission import Missions
from app.db.models.target import Target
from app.gql.types.mission_type import MissionsType


class Query(ObjectType):
    mission_by_id = Field(MissionsType, mission_id=Int(required=True))

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        with session_maker() as session:
            session.query(Missions).filter(Missions.mission_id == mission_id).first()

    mission_by_dates = List(MissionsType, start_date=Date(required=True), end_date=Date(required=True))

    @staticmethod
    def resolve_mission_by_dates(root, info, start_date, end_date):
        with session_maker() as session:
            return (session.query(Missions)
                    .filter(Missions.mission_date >= start_date and Missions.mission_date <= end_date)
                    .all())

    mission_by_country = List(MissionsType, country=String(required=True))

    @staticmethod
    def resolve_mission_by_country(root, info, country):
        with session_maker() as session:
            return (session.query(Missions)
                    .join(Target)
                    .join(City)
                    .join(Country)
                    .filter(Country.country_name == country)
                    .all())

    mission_by_target_industry = List(MissionsType, target_industry=String(required=True))

    @staticmethod
    def resolve_mission_by_target_industry(root, info, target_industry):
        with session_maker() as session:
            return (session.query(Missions)
                    .join(Target)
                    .filter(Target.target_industry == target_industry)
                    .all())

    

