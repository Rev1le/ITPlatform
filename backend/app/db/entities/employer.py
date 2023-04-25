import datetime
from pydantic import BaseModel
from sqlalchemy import Table, Column, Integer, String, Date, Text, ForeignKey
from . import metadata


class Employer(BaseModel):
    uuid: str


employers_table = Table(
    "employer",
    metadata,
    Column('uuid', String(128), primary_key=True),
)
