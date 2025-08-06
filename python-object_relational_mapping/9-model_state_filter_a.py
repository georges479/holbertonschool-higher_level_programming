#!/usr/bin/python3
"""
Lists all State objects containing the letter 'a'
from the database hbtn_0e_6_usa.

Usage:
    ./9-model_state_filter_a.py <mysql username> <mysql password> <database name>

Connects to the MySQL database using SQLAlchemy ORM and
prints all State objects whose name contains the letter 'a',
ordered by id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def main():
    """Connect to the database and print State objects with 'a' in their name."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        if 'a' in state.name:
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()
