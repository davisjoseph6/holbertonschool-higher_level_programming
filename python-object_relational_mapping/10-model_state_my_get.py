#!/usr/bin/python3
"""script that prints the State from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, db))
    Session = sessionmaker(bind=engine)
    session_encap = Session()

    state = session_encap.query(State).filter_by(name=state_name).first()
    print("{}".format(state.id) if state is not None else "Not found")

    session_encap.close()
