# import
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# local import



# orm database engine obj
# ---------------------------------------------------
engine = create_engine('', echo=False)

# orm session obj
session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# BASE class obj for db models
BASE = declarative_base()


# session handler
# ---------------------------------------------------
def db_session_manager():
    # instance session obj
    db_session = session()

    # yield object
    try:
        yield db_session

    finally:
        db_session.close()
