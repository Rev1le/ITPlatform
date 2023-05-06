from pydantic import BaseModel
from sqlalchemy import Table, Column, String, Integer, Float, Text, ForeignKey

from . import metadata


class Vacancy(BaseModel):
    uuid: str
    name: str
    description: str
    salary: str | None
    company: str
    author_uuid: str
    skills: list[str]


vacancies_table = Table(
    'vacancy',
    metadata,
    Column('uuid', String(128), primary_key=True),
    Column('name', String(128)),
    Column('description', Text),
    Column('salary', Float),
    Column('company', String(128)),
    Column('author_uuid', ForeignKey('employer.uuid')),
)