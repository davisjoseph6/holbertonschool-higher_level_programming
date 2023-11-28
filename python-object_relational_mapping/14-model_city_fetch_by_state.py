#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

from model_city import Base, City
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(username, password, database))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    States = session.query(State, City).filter(State.id ==
                                               City.state_id).order_by(City.id)
    for state, cities in States:
        print("{}: ({}) {}".format(state.name, cities.id, cities.name))
    session.close()
