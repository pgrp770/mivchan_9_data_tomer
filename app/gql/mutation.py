from graphene import ObjectType

from app.gql.mutations.mission_mutation import AddMission, UpdateMission
from app.gql.mutations.target_mutation import AddTarget


class Mutation(ObjectType):
    add_mission = AddMission.Field()
    update_mission = UpdateMission.Field()
    
    add_target = AddTarget.Field()