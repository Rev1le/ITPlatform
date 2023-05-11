import datetime

from pydantic import BaseModel, Field
from sqlalchemy import Table, Column, String, ForeignKey, Float

from app.db.entities import User, ResponseUser
from . import metadata


class Mentor(BaseModel):
    user: User
    salary: float
    resume: str
    skills: list[str]


class ResponseMentor(BaseModel):
    user: ResponseUser
    salary: float
    resume: str
    skills: list[str]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


mentors_table = Table(
    'mentor',
    metadata,
    Column('uuid', ForeignKey('user.uuid'), primary_key=True),
    Column('salary', Float),
    Column('resume', String(128))
)