#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)"""


import MySQLdb
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State)
    cities = cities.filter(City.state_id == State.id)
    cities = cities.order_by(City.id)

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
