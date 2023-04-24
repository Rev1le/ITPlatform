from typing import List
from pydantic import BaseModel
import datetime
from sqlalchemy import Table, Column, Integer, String, Text, Date, ARRAY, ForeignKey
from . import metadata


class JobApplicant(BaseModel):
    uuid: str
    name: str
    birthday: datetime.datetime
    password_hash: str
    email: str
    bio: str | None
    photo: str | None
    resume: str | None
    skills: List[str]


job_applicant_table = Table(
    'job_applicants',
    metadata,
    Column('uuid', String(128), primary_key=True),
    Column('name', String(128), nullable=False),
    Column('birthday', Date, nullable=False),
    Column('password_hash', String(40), nullable=False),
    Column('email', String(128), nullable=False, unique=True),
    Column('bio', Text),
    Column('photo', Text),
    Column('resume', Text),
    Column('skills', Text),
)