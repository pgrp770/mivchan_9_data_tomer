from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base



class Target(Base):
    __tablename__ = "targets"
    target_id = Column(Integer, primary_key=True, autoincrement=True)

    mission_id = Column(Integer, ForeignKey("missions.mission_id"))
    mission = relationship("Mission", back_populates="target")

    city_id = Column(Integer, ForeignKey("cities.city_id"))
    city = relationship("City", back_populates="targets")

    target_type_id = Column(Integer, ForeignKey("targettypes.target_type_id"))
    target_type = relationship("TargetTypes", back_populates="targets")

    target_industry = Column(String)
    target_priority = Column(Integer)