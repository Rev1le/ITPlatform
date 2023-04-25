from pydantic import BaseModel
from sqlalchemy import Table, Column, Integer, String, Sequence, Identity
from . import metadata


class Skill(BaseModel):
    uuid: str
    name: str


skills_table = Table(
    'skill',
    metadata,
    Column('uuid', String(128), primary_key=True),
    Column('name', String(128), unique=True, nullable=False),
)