#!/usr/bin/python3
"""script that changes the name of a State object from
the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_update = session.query(State).filter(State.id == '2').first()
    state_update.name = 'New Mexico'
    session.commit()
    session.close()
