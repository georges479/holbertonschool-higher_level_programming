#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa.

Usage:
    ./14-model_city_fetch_by_state.py <mysql username> <mysql password> <database name>

Connects to the MySQL database using SQLAlchemy ORM,
fetches all cities joined with their states,
and prints them ordered by city id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


def main():
    """Fetch and print all cities with their state names."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities joined with states ordered by city id
    query = session.query(City, State).filter(City.state_id == State.id).order_by(City.id)

    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))


if __name__ == "__main__":
    main()
