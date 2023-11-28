#!/usr/bin/python3
"""script that adds the State  e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db))
    Session = sessionmaker(bind=engine)
    session_encap = Session()

    new_state = State(name="Louisiana")
    session_encap.add(new_state)
    session_encap.commit()

    print(new_state.id)

    session_encap.close()
