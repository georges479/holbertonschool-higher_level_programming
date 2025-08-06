#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.

Usage: ./script.py <mysql username> <mysql password> <database name>

- Uses SQLAlchemy
- Imports State and Base from model_state
- Connects to MySQL on localhost at port 3306
- Code not executed when imported
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connexion à la base MySQL
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Sélection et suppression des états dont le nom contient 'a'
    states_to_delete = session.query(State)\
        .filter(State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()
