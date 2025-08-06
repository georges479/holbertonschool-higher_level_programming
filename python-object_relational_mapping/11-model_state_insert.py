#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.

Usage:
    ./11-model_state_insert.py <mysql username> <mysql password> <database name>

Connects to the MySQL database using SQLAlchemy ORM,
creates a new State object with the name "Louisiana",
adds it to the current session, commits the session,
and prints the id of the newly added state.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def main():
    """Create and add a new State named 'Louisiana' to the database."""
    # Create the SQLAlchemy engine to connect to the MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session instance
    session = Session()

    # Instantiate a new State object with name "Louisiana"
    louisiana = State(name="Louisiana")
    # Add the new object to the session
    session.add(louisiana)
    # Commit the session to save the new State to the database
    session.commit()
    # Print the id of the new State object (assigned by the database)
    print(louisiana.id)


if __name__ == "__main__":
    main()
