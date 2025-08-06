#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.

Usage: ./script.py <mysql username> <mysql password> <database name>

- Uses SQLAlchemy
- Imports State and Base from model_state
- Connects to MySQL on localhost at port 3306
- Prints the first State by states.id ascending
- Prints "Nothing" if no state found
- Does not fetch all states before displaying the result
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query only the first state ordered by id, without loading all states
    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")
