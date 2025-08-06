#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.

Usage: ./script.py <mysql username> <mysql password>
<database name> <state name>

- Uses SQLAlchemy
- Imports State and Base from model_state
- Connects to MySQL on localhost at port 3306
- SQL injection safe
- Prints state.id if found, otherwise prints "Not found"
- Code not executed when imported
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine and session
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State filtering by name safely using filter
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")
