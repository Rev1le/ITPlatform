import datetime
from pydantic import BaseModel
from sqlalchemy import Table, Column, Integer, String, Date, Text
from . import metadata


class Employer(BaseModel):
    name: str
    birthday: datetime.datetime
    password_hash: str
    email: str
    bio: str | None
    photo: str | None


employers_table = Table(
    "employers",
    metadata,
    Column('uuid', String(128), primary_key=True, nullable=False),
    Column('name', String(128), nullable=False),
    Column('birthday', Date, nullable=False),
    Column('password_hash', String(40), nullable=False),
    Column('email', String(128), nullable=False, unique=True),
    Column('bio', Text),
    Column('photo', Text),
)
