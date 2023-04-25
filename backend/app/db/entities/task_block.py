from pydantic import BaseModel
from sqlalchemy import Table, Column, Integer, String, Text
from . import metadata


class TaskBlock(BaseModel):
    uuid: str
    name: str
    difficulty: str
    description: str

task_blocks_table = Table(
    'task_blocks',
    metadata,
    Column('uuid', String(128), primary_key=True),
    Column('name', String(128), nullable=False),
    Column('difficulty', Integer, nullable=False),
    Column('description', Text),
)


# required property name -> str;
#         required property difficulty -> int16;
#         required property description -> str;
#         multi link questions -> TaskQuestion;
#         multi link codes -> TaskCode;
#         multi link completed -> Worker;
#         multi link failed -> Worker;