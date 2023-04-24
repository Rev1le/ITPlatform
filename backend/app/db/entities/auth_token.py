from pydantic import BaseModel
from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey
from . import metadata


class AuthToken(BaseModel):
    token: str
    owner_uuid: str


tokens_table = Table(
    'tokens',
    metadata,
    Column('token', String(128), nullable=False, primary_key=True),
    Column('owner_uuid', ForeignKey("employers.uuid"))
)