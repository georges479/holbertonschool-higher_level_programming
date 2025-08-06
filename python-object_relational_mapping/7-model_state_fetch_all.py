#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.

Usage:
    ./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>

Connects to the MySQL database using SQLAlchemy ORM and
prints all State objects sorted by their id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def main():
    """Connect to the database and display all State objects sorted by id."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()
