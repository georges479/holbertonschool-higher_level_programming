#!/usr/bin/python3
"""
Lists the State object with the name passed as argument
from the database hbtn_0e_6_usa.

Usage:
    ./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state name searched>

Connects to the MySQL database using SQLAlchemy ORM,
searches for the first State object with the specified name,
and prints its id. If no state is found, prints "Not found".
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def main():
    """Connect to the database and print the id of the State with the given name."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break

    if not found:
        print("Not found")


if __name__ == "__main__":
    main()
