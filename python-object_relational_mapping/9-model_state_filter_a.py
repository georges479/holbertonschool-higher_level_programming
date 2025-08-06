#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.

Usage: ./script.py <mysql username> <mysql password> <database name>

- Uses SQLAlchemy
- Imports State and Base from model_state
- Connects to MySQL on localhost at port 3306
- Results sorted ascending by states.id
- Displays results as: "<id>: <name>"
- Code not executed when imported
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
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

    # Filter states with 'a' in their name and order by id ascending
    states_with_a = session.query(State)\
        .filter(State.name.like('%a%')).order_by(State.id)

    for state in states_with_a:
        print(f"{state.id}: {state.name}")
