#!/usr/bin/env python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states_with_a(username, password, db_name):
    # Create the engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}', echo=False)
    
    # Initialize the session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query to find states containing the letter 'a'
    query = session.query(State).filter(State.name.contains('a')).order_by(State.id.asc())
    
    # Execute the query and print the results
    for state in query.all():
        print(f"{state.id}: {state.name}")
    
    # Close the session
    session.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    list_states_with_a(username, password, db_name)