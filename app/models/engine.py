from sqlmodel import Session, create_engine

from app.core.settings import Settings

engine = create_engine(Settings().DB_CONNECTION_STRING)

def db_session():
    with Session(engine) as session:
        yield session
