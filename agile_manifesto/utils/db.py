from sqlalchemy.orm import sessionmaker


def materialize_schema(Base, engine):
    Base.metadata.create_all(engine)


def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
