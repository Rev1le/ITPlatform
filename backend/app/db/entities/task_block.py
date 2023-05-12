import json
import uuid

from pydantic import BaseModel, validator, Field
from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey, Boolean
from . import metadata


def create_uuid_str():
    return str(uuid.uuid4())


class TaskBlock(BaseModel):
    uuid: str = Field(default_factory=create_uuid_str)
    name: str
    difficulty: int
    description: str | None
    questions_json: str

    @validator('difficulty')
    def difficulty_must_in_range(cls, v):
        if v not in range(1, 6):
            raise ValueError('difficulty not in range(1, 6)')
        return v


class QuestionVariantResponse(BaseModel):
    content: str


class QuestionResponse(BaseModel):
    uuid: str
    body: str
    variants: list[QuestionVariantResponse]


class TaskBlockResponse(BaseModel):
    uuid: str
    name: str
    difficulty: int
    description: str | None
    questions: list[QuestionResponse]

    @validator('difficulty')
    def difficulty_must_in_range(cls, v):
        if v not in range(1, 6):
            raise ValueError('difficulty not in range(1, 6)')
        return v

    @classmethod
    def from_task_block(cls, task_block: TaskBlock):
        dict_row = dict(task_block)
        questions_str = dict_row.pop('questions_json')

        questions = json.loads(questions_str)
        dict_row['questions'] = questions

        return cls(**dict_row)


task_blocks_table = Table(
    'task_block',
    metadata,
    Column('uuid', String(128), primary_key=True),
    Column('name', String(128), nullable=False),
    Column('difficulty', Integer, nullable=False),
    Column('description', Text),
    Column('questions_json', Text, nullable=False),
)
