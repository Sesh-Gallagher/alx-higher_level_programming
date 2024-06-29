#!/usr/bin/python3
""" Module that lists all state objects using sqlalchemy """

if __name__ == '__main__':

    from sqlalchemy.orm.session import sessionmaker, Session
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sys import argv

    db_name = '{}'.format(argv[3])
    username = '{}'.format(argv[1])
    password = '{}'.format(argv[2])

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print('{}: {}'.format(state.id, state.name))
