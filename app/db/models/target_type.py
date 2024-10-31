from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.db.models import Base


class TargetTypes(Base):
    __tablename__ = "targettypes"
    target_type_id = Column(Integer)
    target_type_name = Column(String)

    targets = relationship("Target", back_populates="target_type")