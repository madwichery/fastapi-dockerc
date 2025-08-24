from sqlmodel import Session, select

from app.models.database import User
from app.schema.user import UserCreate


def create_user(db_session: Session, user: UserCreate):
    new_user = User(**user.model_dump())
    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)
    return new_user

    # Jika mengunakan Session
    # with Session(engine) as session:
    #     db_user = User(**user.model_dump())

    #     session.add(db_user)
    #     session.commit()
    #     session.refresh(db_user)
    #     return db_user


def get_user(db_session: Session, user_id: str):

    # cara pertama paling umum
    # statement = select(User).options(selectinload(User.posts)).where(User.id == user_id)

    # cara kedua : lazy load
    statement = select(User).where(User.id == user_id)
    user = db_session.exec(statement).first()

    _ = user.posts # melakukan lazy query
    return user

    return db_session.exec(statement).first()

def get_users(db_session: Session):
    return db_session.exec(select(User)).all()
