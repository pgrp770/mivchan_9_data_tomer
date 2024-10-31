from graphene import ObjectType, Int, String, Float, Field

from app.db.database import session_maker
from app.db.models.country import Country
from app.gql.types.countries_type import CountryType


class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    latitude = Float()
    longitude = Float()

    country_id = Int()
    country = Field(CountryType)

    @staticmethod
    def resolve_country(root, info):
        with session_maker() as session:
            return session.query(Country).filter(Country.country_id == root.country_id)
