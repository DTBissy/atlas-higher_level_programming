#!/usr/bin/python3
"""Connects to a SQLserver"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    username=sys.argv[1]
    password=sys.argv[2]
    db=sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/\
                           {db}')
    
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    first = session.query(State).order_by(State.id).first()
    if first:
        print(f"{first.id}: {first.name}")
    else:
        print("Nothing")

    Session.close()