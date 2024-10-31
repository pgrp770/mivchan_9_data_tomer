from graphene import ObjectType, Field, Int, List, Date

from app.db.database import session_maker
from app.db.models.mission import Missions
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

    
