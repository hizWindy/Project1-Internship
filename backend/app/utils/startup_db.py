from db.database import engine
import sqlalchemy


def startup_db():
    with engine.connect() as connection:
        connection._is_disconnect
