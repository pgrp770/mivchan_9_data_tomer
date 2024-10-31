from graphene import Mutation, Int, Field, String

from app.db.database import session_maker
from app.db.models import Target


from app.gql.types.target_types import TargetType


class AddTarget(Mutation):
    class Arguments:
        target_id = Int(required=True)
        mission_id = Int(required=True)
        city_id = Int(required=True)
        target_type_id = Int(required=True)
        target_industry = String(required=True)
        target_priority = Int(required=True)

    target = Field(TargetType)

    @staticmethod
    def mutate(root,
               info,
               target_id,
               mission_id,
               city_id,
               target_type_id,
               target_industry,
               target_priority):
        with session_maker() as session:
            new_target = Target(
                target_id=target_id,
                mission_id=mission_id,
                city_id=city_id,
                target_type_id=target_type_id,
                target_industry=target_industry,
                target_priority=target_priority
            )
            session.add(new_target)
            session.commit()
            session.refresh(new_target)
            return AddTarget(target=new_target)
