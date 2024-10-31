from app.db.database import session_maker
from app.db.models import Missions, Target, City, Country, TargetTypes


def get_mission_by_id(mission_id):
    with session_maker() as session:
        return session.query(Missions).filter(Missions.mission_id == mission_id).first()


def get_mission_between_dates(start_date, end_date):
    with session_maker() as session:
        return (session.query(Missions)
                .filter(Missions.mission_date.between(start_date, end_date))
                .all())


def get_mission_by_country(country):
    with session_maker() as session:
        return (session.query(Missions)
                .join(Target)
                .join(City)
                .join(Country)
                .filter(Country.country_name == country)
                .all())


def get_mission_by_target_industry(target_industry):
    with session_maker() as session:
        return (session.query(Missions)
                .join(Target)
                .filter(Target.target_industry == target_industry)
                .all())


def get_mission_by_target_type(target_type):
    with session_maker() as session:
        return (session.query(Missions)
                .join(Target)
                .join(TargetTypes)
                .filter(TargetTypes.target_type_name == target_type)
                .all())
