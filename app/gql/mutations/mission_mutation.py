from graphene import Mutation, Date, Float, Field, Int, Boolean, String
from returns.result import Failure

from app.db.database import session_maker
from app.db.models import Missions, Target
from app.gql.types.mission_type import MissionsType
from sqlalchemy.sql.expression import func

from app.repository.mission_repository import delete_mission


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


class UpdateMission(Mutation):
    class Arguments:
        mission_id = Int(required=True)
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
               mission_id,
               mission_date,
               airborne_aircraft,
               attacking_aircraft,
               bombing_aircraft,
               aircraft_returned,
               aircraft_failed,
               aircraft_damaged,
               aircraft_lost):
        with session_maker() as session:
            maybe_mission = session.query(Missions).filter(Missions.mission_id == mission_id).first()
            if maybe_mission is None:
                raise Exception("there is on mission with this id")

            maybe_mission.mission_date = mission_date,
            maybe_mission.airborne_aircraft = airborne_aircraft,
            maybe_mission.attacking_aircraft = attacking_aircraft,
            maybe_mission.bombing_aircraft = bombing_aircraft,
            maybe_mission.aircraft_returned = aircraft_returned,
            maybe_mission.aircraft_failed = aircraft_failed,
            maybe_mission.aircraft_damaged = aircraft_damaged,
            maybe_mission.aircraft_lost = aircraft_lost

            session.commit()
            session.refresh(maybe_mission)
            return AddMission(mission=maybe_mission)


class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int(required=True)

    success = Boolean()
    message = String()

    @staticmethod
    def mutate(root, info, mission_id,):
        res = delete_mission(mission_id)
        if isinstance(res, Failure):
            return DeleteMission(success=False, message=res.failure())
        return DeleteMission(success=True, message="you have successfully deleted the mission with the related target")
