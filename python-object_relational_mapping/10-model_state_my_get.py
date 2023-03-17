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

    state_name = State.name.like(sys.argv[4])
    state = session.query(State).filter(state_name).first()

    if state:
        print(f'{state.id}')
    else:
        print('Not found')

    session.commit()
    session.close()
