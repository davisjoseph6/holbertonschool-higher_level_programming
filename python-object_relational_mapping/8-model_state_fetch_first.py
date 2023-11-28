#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db))
    Session = sessionmaker(bind=engine)
    session_encap = Session()

    first_state = session_encap.query(State).order_by(State.id).first()

    print("{}: {}".format(first_state.id, first_state.name)
          if first_state is not None else "Nothing")

    session_encap.close()
