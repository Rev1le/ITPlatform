from pydantic import BaseModel
from sqlalchemy import Table, Column, String, ForeignKey, Float
from . import metadata

mentor_skills_table = Table(
    'mentor_skill',
    metadata,
    Column('mentor_uuid', ForeignKey('mentor.uuid'), primary_key=True),
    Column('skill_uuid', ForeignKey('skill.uuid'), primary_key=True)
)