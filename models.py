from sqlalchemy import Column,Integer,DateTime,String,ForeignKey,create_engine,func
from sqlalchemy.orm import declarative_base,relationship,sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=engine)
session = Session()

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer,primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    department_id = Column(Integer,ForeignKey('departments.id'))
    position_id = Column(Integer,ForeignKey('positions.id'))
    hire_date = Column(DateTime,default=func.now())

    position = relationship('Position', back_populates="employees")
    department = relationship('Department', back_populates="employees")


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    employees = relationship('Employee', back_populates="department")
    positions = relationship('Position', back_populates="department")




class Position(Base):
    __tablename__ = "positions"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    department_id = Column(Integer,ForeignKey('departments.id'))

    employees = relationship('Employee', back_populates="position")
    department = relationship('Department', back_populates="positions")

