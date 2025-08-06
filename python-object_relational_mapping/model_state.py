#!/usr/bin/python3
"""Module that defines the State class and Base for SQLAlchemy ORM"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Base instance for class inheritance
Base = declarative_base()

class State(Base):
    """State class mapped to the 'states' MySQL table"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # This block only runs if the file is executed directly
    # Create engine and create all tables in the database
    engine = create_engine("mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa",
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
