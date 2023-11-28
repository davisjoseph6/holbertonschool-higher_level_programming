#!/usr/bin/python3
"Lists all State objects that contain the letter a"

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id)
    for state in query.filter(State.name.like('%a%')):
        print(f"{state.id}: {state.name}")
