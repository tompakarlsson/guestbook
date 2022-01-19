from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from typing import List

from guestbook.database import get_session
from guestbook.models import User, UserCreate, NoteReadFromUser, UserRead
from guestbook import crud
from guestbook.crud.users import get_user
from sqlmodel import Session, select

users = APIRouter()


@users.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, session: Session = Depends(get_session)):
    """read user specified by user_id"""

    return get_user(session=session, user_id=user_id)


@users.get("/", response_model=List[UserRead])
def read_users(session: Session = Depends(get_session)):
    """read all users"""

    all_users: List[User] = session.exec(select(User)).all()
    return all_users


@users.get("/note_from_user/{user_id}", response_model=NoteReadFromUser)
def read_notes_from_user(*, user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    return user


@users.post("/", response_model=User)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    """create user"""

    return crud.users.create_user(session=session, user=user)


@users.delete("/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    """Remove user"""

    user: User = get_user(session=session, user_id=user_id)
    session.delete(user)
    session.commit()
    return JSONResponse(
        f"Removed User: {user_id}",
        status_code=status.HTTP_200_OK,
    )
