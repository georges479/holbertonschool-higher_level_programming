#!/usr/bin/python3
"""
Deletes all State objects containing the letter 'a'
from the database hbtn_0e_6_usa.

Usage:
    ./13-model_state_delete_a.py <mysql username> <mysql password> <database name>

Connects to the MySQL database using SQLAlchemy ORM,
finds all State objects with 'a' in their name,
deletes them from the database,
and commits the changes.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def main():
    """Delete all State objects with 'a' in their name."""
    # Create engine to connect to the database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    # Create a session class
    Session = sessionmaker(bind=engine)
    # Create a session instance
    session = Session()

    # Iterate over all State objects
    for state in session.query(State):
        if "a" in state.name:
            # Delete states whose name contains 'a'
            session.delete(state)
    # Commit the transaction to apply the deletions
    session.commit()


if __name__ == "__main__":
    main()
