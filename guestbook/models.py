"""Create models for SQLModel"""

from datetime import datetime
from typing import List, Optional

from sqlmodel import SQLModel, Field, Relationship


class UserBase(SQLModel):
    username: str
    user_email: str
    user_full_name: Optional[str]


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    notes: List["Note"] = Relationship(back_populates="user")


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int


class NoteBase(SQLModel):
    """
    Data model used for accessing notes from db
    """
    note: str = Field(index=True)
    created_at: Optional[datetime] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")


class Note(NoteBase, table=True):
    """
    Pydantic/SQLAlchemy model which represents Note table in db. Inherits from data model NoteBase.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    user: Optional[User] = Relationship(back_populates="notes")


class NoteRead(NoteBase):
    id: int


class NoteCreate(NoteBase):
    """Create Note"""
    pass


class NoteUpdate(SQLModel):
    """Update note specified by id"""
    note: Optional[str] = None
    created_at: Optional[datetime] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#    user: Optional[str] = None


class NoteReadFromUser(UserBase):
    """Read all notes from a specified user"""
    id: int
    notes: List[Note]