import uuid

from pydantic import BaseModel, validator, Field
from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey, Boolean
from . import metadata


def create_uuid_str():
    return str(uuid.uuid4())


class CodeTask(BaseModel):
    text: str


class QuestionVariant(BaseModel):
    content: str
    is_answer: bool


class Question(BaseModel):
    uuid: str = Field(default_factory=create_uuid_str)
    body: str
    variants: list[QuestionVariant]


class TaskBlock(BaseModel):
    uuid: str
    name: str
    difficulty: int
    description: str | None
    questions: list[Question]
    #code_tasks: list[CodeTask]

    @validator('difficulty')
    def difficulty_must_in_range(cls, v):
        if v not in range(1, 6):
            raise ValueError('difficulty not in range(1, 6)')
        return v


task_blocks_table = Table(
    'task_block',
    metadata,
    Column('uuid', String(128), primary_key=True),
    Column('name', String(128), nullable=False),
    Column('difficulty', Integer, nullable=False),
    Column('description', Text),
)

questions_table = Table(
    'question',
    metadata,
    Column('task_block_uuid', ForeignKey('task_block.uuid')),
    Column('uuid', String(128), primary_key=True),
    Column('body', Text, nullable=False),
)

question_options_table = Table(
    'question_variant',
    metadata,
    Column('question_uuid', ForeignKey('question.uuid')),
    Column('content', Text, nullable=False),
    Column('is_answer', Boolean, nullable=False),
)
