from graphene import Mutation, Date, Float, Field

from app.db.database import session_maker
from app.db.models import Missions
from app.gql.types.mission_type import MissionsType
from sqlalchemy.sql.expression import func



class AddMission(Mutation):
    class Arguments:
        mission_date = Date(required=True)
        airborne_aircraft = Float(required=True)
        attacking_aircraft = Float(required=True)
        bombing_aircraft = Float(required=True)
        aircraft_returned = Float(required=True)
        aircraft_failed = Float(required=True)
        aircraft_damaged = Float(required=True)
        aircraft_lost = Float(required=True)

    mission = Field(MissionsType)


    @staticmethod
    def mutate(root,
               info,
               mission_date,
               airborne_aircraft,
               attacking_aircraft,
               bombing_aircraft,
               aircraft_returned,
               aircraft_failed,
               aircraft_damaged,
        aircraft_lost):

        with session_maker() as session:
            mission_id = session.query(func.max(Missions.mission_id)).scalar() + 1
            new_mission = Missions(
                mission_id=mission_id,
                mission_date=mission_date,
                airborne_aircraft=airborne_aircraft,
                attacking_aircraft=attacking_aircraft,
                bombing_aircraft=bombing_aircraft,
                aircraft_returned=aircraft_returned,
                aircraft_failed=aircraft_failed,
                aircraft_damaged=aircraft_damaged,
                aircraft_lost=aircraft_lost
            )
            session.add(new_mission)
            session.commit()
            session.refresh(new_mission)
            return AddMission(mission=new_mission)