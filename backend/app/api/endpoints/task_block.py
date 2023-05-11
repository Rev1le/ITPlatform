import pprint
import uuid
from typing import List

from pydantic import BaseModel, ValidationError, validator
from fastapi import APIRouter

from app.api.deps import AuthUser
from app.db.entities import TaskBlock
from app.db.queries.create.create_task_block_async import create_task_block as db_create_task_block
from app.db.queries.get.get_task_block_async import get_task_block as db_get_task_block


class QuestionVariantData(BaseModel):
    content: str
    is_answer: bool


class QuestionData(BaseModel):
    body: str
    variants: list[QuestionVariantData]


class TaskBlockData(BaseModel):
    name: str
    difficulty: int
    description: str | None
    questions: List[QuestionData]

    @validator('difficulty')
    def difficulty_must_in_range(cls, v):
        if v not in range(1, 6):
            raise ValueError('difficulty not in range(1, 6)')
        return v


router = APIRouter()


@router.get("/all")
async def get_all_task_blocks() -> list[TaskBlock]:
    await db_get_task_block("015050cc-afa7-4a75-b111-ee34582878f4")
    return []


@router.post("/")
async def create_task_block(user: AuthUser, task_block_data: TaskBlockData):
    print(task_block_data.dict())

    task_block = TaskBlock(uuid=str(uuid.uuid4()), **task_block_data.dict())

    pprint.pprint(task_block.dict())

    await db_create_task_block(task_block)
