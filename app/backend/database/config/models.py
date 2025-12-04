# import
from sqlalchemy import Column, ForeignKey, Identity, func, Integer, String, Boolean, LargeBinary, DateTime, Date, Float, Time
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.dialects.mysql import DECIMAL
from sqlalchemy.orm import relationship

# local import
from app.backend.database.config.config import BASE


# models
# ---------------------------------------------------

class Province(BASE):
    __tablename__ = "province"
    __table_args__ = {"schema": "cat"}
    id = Column(Integer, Identity(start=100, increment=1, cycle=False), primary_key=True)
    name = Column(String(75), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    # relationship
    cantons = relationship("Canton", back_populates="province", cascade="all, delete-orphan")

    # __rep__
    def __repr__(self):
        return (f"<Province(id={self.id}, name={self.name}, created_at={self.created_at}, "
                f"updated_at={self.updated_at})>")


class Canton(BASE):
    __tablename__ = "canton"
    __table_args__ = {"schema": "cat"}
    id = Column(Integer, Identity(start=200, increment=1, cycle=False), primary_key=True)
    name = Column(String(75), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    # foreign key
    id_province = Column(Integer, ForeignKey("cat.province.id"), nullable=False)
    # relationship
    province = relationship("Province", back_populates="cantons")
    districts = relationship("District", back_populates="canton", cascade="all, delete-orphan")

    # __rep__
    def __repr__(self):
        return (f"<Canton(id={self.id}, name={self.name}, id_province={self.id_province}, "
                f"created_at={self.created_at}, updated_at={self.updated_at})>")


class District(BASE):
    __tablename__ = "district"
    __table_args__ = {"schema": "cat"}
    id = Column(Integer, Identity(start=300, increment=1, cycle=False), primary_key=True)
    name = Column(String(75), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    # foreign key
    id_canton = Column(Integer, ForeignKey("cat.canton.id"), nullable=False)
    # relationship
    canton = relationship("Canton", back_populates="districts")

    # __rep__
    def __repr__(self):
        return (f"<District(id={self.id}, name={self.name}, id_canton={self.id_canton}, "
                f"created_at={self.created_at}, updated_at={self.updated_at})>")
