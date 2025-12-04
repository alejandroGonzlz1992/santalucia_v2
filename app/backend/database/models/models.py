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
    addresses = relationship("Address", back_populates="district", cascade="all, delete-orphan")

    # __rep__
    def __repr__(self):
        return (f"<District(id={self.id}, name={self.name}, id_canton={self.id_canton}, "
                f"created_at={self.created_at}, updated_at={self.updated_at})>")


class Address(BASE):
    __tablename__ = "address"
    __table_args__ = {"schema": "cat"}
    id = Column(Integer, Identity(start=400, increment=1, cycle=False), primary_key=True)
    details = Column(String(450), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    # foreign key
    id_district = Column(Integer, ForeignKey("cat.district.id"), nullable=False)
    # relationship
    district = relationship("District", back_populates="addresses")

    # __rep__
    def __repr__(self):
        return (f"<Address(id={self.id}, details={self.details}, id_district={self.id_district}, "
                f"created_at={self.created_at}, updated_at={self.updated_at})>")


class Department(BASE):
    __tablename__ = "department"
    __table_args__ = {"schema": "cat"}
    id = Column(Integer, Identity(start=500, increment=1, cycle=False), primary_key=True)
    name = Column(String(75), nullable=False)
    description = Column(String(450), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    # relationship
    positions = relationship("Position", back_populates="department", cascade="all, delete-orphan")

    # __rep__
    def __repr__(self):
        return (f"<Department(id={self.id}, name={self.name}, description={self.description}, "
                f"created_at={self.created_at}, updated_at={self.updated_at})>")


class Position(BASE):
    __tablename__ = "position"
    __table_args__ = {"schema": "cat"}
    id = Column(Integer, Identity(start=600, increment=1, cycle=False), primary_key=True)
    name = Column(String(75), nullable=False)
    description = Column(String(450), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    # foreign key
    id_department = Column(Integer, ForeignKey("cat.department.id"), nullable=False)
    # relationship
    department = relationship("Department", back_populates="positions")

    # __rep__
    def __repr__(self):
        return (f"<Position(id={self.id}, name={self.name}, description={self.description}, "
                f"id_department={self.id_department}, created_at={self.created_at}, "
                f"updated_at={self.updated_at})>")


class Contract(BASE):
    __tablename__ = "contract"
    __table_args__ = {"schema": "cat"}
    id = Column(Integer, Identity(start=700, increment=1, cycle=False), primary_key=True)
    name = Column(String(75), nullable=False)
    description = Column(String(450), nullable=False)
    is_temporal = Column(Boolean, nullable=False, default=False)
    durantion_month = Column(Integer, nullable=False, server_default="3")
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    # relationship


    # __rep__
    def __repr__(self):
        return (f"<Contract(id={self.id}, name={self.name}, description={self.description}, "
                f"is_temporal={self.is_temporal}, durantion_month={self.durantion_month}, "
                f"created_at={self.created_at}, updated_at={self.updated_at})>")


class EmployeeStatus(BASE):
    __tablename__ = "employeestatus"
    __table_args__ = {"schema": "cat"}
    id = Column(Integer, Identity(start=800, increment=1, cycle=False), primary_key=True)
    name = Column(String(75), nullable=False)
    description = Column(String(450), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)


