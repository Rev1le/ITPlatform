from sqlalchemy import Table, Column, Integer, String, Text, Date, ARRAY, ForeignKey
from . import metadata

skills_table = Table(
    'skills',
    metadata,
    Column('name', String(128), primary_key=True)
)