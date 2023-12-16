#!/usr/bin/python3

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import asc

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    results = session.query(State).\
        join(City).filter(State.id == City.state_id).\
        order_by(asc(City.id)).all()

    for state in results:
        for city in state.cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
    engine.dispose()
