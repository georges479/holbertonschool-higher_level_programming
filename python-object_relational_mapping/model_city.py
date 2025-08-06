#!/usr/bin/python3
"""
Contains the class definition of a City

- Inherits from Base (imported from model_state)
- Links to the MySQL table cities
- Attributes:
  - id: primary key, integer, auto-increment, not null
  - name: string(128), not null
  - state_id: integer, not null, foreign key to states.id
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """City class that represents the cities table in MySQL database"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
