#!/usr/bin/python3
"""
Prints all City objects from  database hbtn_0e_14_us
"""
import sys
from model_state import State
from model_city import City, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    st_cty = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in st_cty:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

# Hassan Munene
