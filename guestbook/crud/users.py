from guestbook.models import User, UserCreate
from sqlmodel import Session, select
from fastapi import HTTPException


def get_user(session: Session, user_id: int) -> User:
    """Get user"""
    statement = select(User).where(User.id == user_id)
    return session.exec(statement).one()


def create_user(session: Session, user: UserCreate) -> User:
    """Adding a user to db"""
    db_user = User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
