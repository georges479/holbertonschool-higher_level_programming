#!/usr/bin/python3
"""
Changes the name of the State object with id = 2 to "New Mexico"
in the database hbtn_0e_6_usa.

Usage:
    ./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>

Connects to the MySQL database using SQLAlchemy ORM,
fetches the State object with id 2,
updates its name to "New Mexico",
and commits the change to the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def main():
    """Update the State name where id is 2 to 'New Mexico'."""
    # Create engine to connect to the MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    # Create a configured session class
    Session = sessionmaker(bind=engine)
    # Instantiate a session
    session = Session()

    # Query the State with id=2
    state = session.query(State).filter_by(id=2).first()
    if state is not None:
        # Update the State's name
        state.name = "New Mexico"
        # Commit the changes
        session.commit()


if __name__ == "__main__":
    main()
