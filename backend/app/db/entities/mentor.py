from pydantic import BaseModel
from sqlalchemy import Table, Column, String, ForeignKey, Float
from . import metadata


class Mentor(BaseModel):
    uuid: str
    salary: float
    resume: str


mentors_table = Table(
    'mentor',
    metadata,
    Column('uuid', ForeignKey('employer.uuid'), primary_key=True),
    Column('salary', Float),
    Column('resume', String(128))
)