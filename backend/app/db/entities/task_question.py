from pydantic import BaseModel
from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey
from . import metadata


task_block_skills_table = Table(
    'task_block_skill',
    metadata,
    Column('task_block_uuid', ForeignKey('task_block.uuid'), primary_key=True),
    Column('skill_uuid', ForeignKey('skill.uuid'), primary_key=True),
)