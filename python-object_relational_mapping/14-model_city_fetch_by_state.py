#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa

Usage: ./14-model_city_fetch_by_state.py <mysql username>
<mysql password> <database name>

- Uses SQLAlchemy
- Imports State and Base from model_state
- Connects to MySQL on localhost port 3306
- Results sorted by cities.id ascending
- Prints results as: <state name>: (<city id>) <city name>
- Code not executed when imported
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Create engine and session
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format
        (sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query City and State with join on state_id
    #  == states.id, sorted by city.id
    query = session.query(City, State)\
        .filter(City.state_id == State.id).order_by(City.id)

    for city, state in query:
        print(f"{state.name}: ({city.id}) {city.name}")
