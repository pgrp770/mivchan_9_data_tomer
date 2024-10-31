from graphene import ObjectType

from app.gql.mutations.mission_mutation import AddMission, UpdateMission, DeleteMission
from app.gql.mutations.target_mutation import AddTarget


class Mutation(ObjectType):
    add_mission = AddMission.Field()
    update_mission = UpdateMission.Field()
    delete_mutation = DeleteMission.Field()
    add_target = AddTarget.Field()