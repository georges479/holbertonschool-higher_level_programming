#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa.

Usage: ./script.py <mysql username> <mysql password> <database name>

- Uses SQLAlchemy
- Imports State and Base from model_state
- Connects to MySQL on localhost at port 3306
- Prints the new state's id after creation
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

    # Create new State object with name "Louisiana"
    new_state = State(name="Louisiana")

    # Add to session and commit
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)
