#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.

Usage: ./script.py <mysql username> <mysql password> <database name>

- Uses SQLAlchemy
- Imports State and Base from model_state
- Connects to MySQL on localhost at port 3306
- Results sorted by states.id ascending
- Results displayed as "<id>: <name>"
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create the engine to connect to the MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()

    # Query all State objects ordered by id
    states = session.query(State).order_by(State.id).all()

    # Print all states as "<id>: <name>"
    for state in states:
        print(f"{state.id}: {state.name}")
