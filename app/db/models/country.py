from sqlalchemy import String, Integer
from sqlalchemy.orm import relationship

from app.db.models import Base


class Country(Base):
    country_id = Integer()
    country_name = String()

    cities = relationship("City", back_populates="country")