"""
Main functions for the guestbook api
"""

from fastapi import status, FastAPI

from guestbook.api.endpoints.notes import notes
from guestbook.api.endpoints.users import users
from guestbook.database import create_db_and_tables

app = FastAPI()


@app.get("/")
def welcome():
    return {"hello": "Welcome to the guestbook"}


app.include_router(
    notes,
    prefix="/notes",
    tags=["notes"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

app.include_router(
    users,
    prefix="/users",
    tags=["users"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
