from pydantic import BaseModel
from sqlalchemy import Table, Column, String, ForeignKey, Float
from . import metadata

vacancy_skills_table = Table(
    'vacancy_skill',
    metadata,
    Column('vacancy_uuid', ForeignKey('vacancy.uuid'), primary_key=True),
    Column('skill_uuid', ForeignKey('skill.uuid'), primary_key=True)
)