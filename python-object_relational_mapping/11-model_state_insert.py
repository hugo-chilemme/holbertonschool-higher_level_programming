#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)"""


import MySQLdb
import sys
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)

    state = session.query(State).order_by(State.id.desc()).first()
    print(state.id)

    session.commit()
    session.close()
