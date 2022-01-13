from fastapi import APIRouter, Depends, status, Query
from fastapi.responses import JSONResponse

from typing import List

from guestbook.database import get_session
from guestbook.models import Note, NoteCreate, NoteUpdate, NoteRead
from guestbook import crud
from guestbook.crud.notes import get_note
from sqlmodel import Session, select

notes = APIRouter()


@notes.get("/{note_id}", response_model=NoteRead)
def read_note(note_id: str, session: Session = Depends(get_session)):
    """read note specified by note_id"""

    return get_note(session=session, note_id=note_id)


@notes.get("/", response_model=List[NoteRead])
def read_notes(
        *,
        session: Session = Depends(get_session),
        limit: int = Query(default=100, lte=100)
):
    """read all notes sorted in descending order"""

    all_notes: List[NoteRead] = session.exec(select(Note).order_by(Note.id.desc()).limit(limit)).all()
    return all_notes


@notes.post("/", response_model=NoteRead)
def create_note(*, session: Session = Depends(get_session), note: NoteCreate):
    """post note"""

    return crud.notes.create_note(session=session, note=note)


@notes.delete("/{note_id}")
def delete_note(*, note_id: str, session: Session = Depends(get_session)):
    """Delete note"""

    note: NoteRead = get_note(session=session, note_id=note_id)
    session.delete(note)
    session.commit()
    return JSONResponse(
        f"Deleted note: {note_id}",
        status_code=status.HTTP_200_OK,
    )

@notes.patch("/{note_id}", response_model=NoteRead)
def update_note(*, session: Session = Depends(get_session), note_id: str, note: NoteUpdate):
    """Update note"""

    return crud.notes.update_note(session=session, note=note, note_id=note_id)
