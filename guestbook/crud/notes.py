from guestbook.models import Note, NoteCreate, NoteUpdate
from sqlmodel import Session, select
from fastapi import HTTPException


def get_note(*, session: Session, note_id: int) -> Note:
    """Get note"""
    statement = select(Note).where(Note.id == note_id)
    return session.exec(statement).one()


def create_note(*, session: Session, note: NoteCreate) -> Note:
    """Adding a note to db"""
    db_note = Note.from_orm(note)
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note


def update_note(*, session: Session, note: NoteUpdate, note_id: int) -> Note:
    """Updating a note"""
    db_note = session.get(Note, note_id)
    note_data = note.dict(exclude_unset=True)
    for key, value in note_data.items():
        setattr(db_note, key, value)
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note