import pprint
import json
import uuid
from typing import List

import pydantic
from pydantic import BaseModel, ValidationError, validator, Field
from fastapi import APIRouter

from app.api.deps import AuthUser
from app.db.entities import TaskBlock, TaskBlockResponse
from app.db.queries.create.create_task_block_async import create_task_block as db_create_task_block
from app.db.queries.get.get_task_block_async import get_task_block as db_get_task_block
from app.db.queries.get.get_all_task_blocks_async import get_all_task_block as db_get_all_task_blocks


def get_uuid_str() -> str:
    return str(uuid.uuid4())


class QuestionVariantData(BaseModel):
    content: str
    is_answer: bool


class QuestionData(BaseModel):
    #uuid: str = Field(default_factory=get_uuid_str)
    body: str
    variants: dict[str, dict]


class ResultQuestionData(BaseModel):
    question_uuid: str
    select_variants_content: list[str]


class ResultTaskBlockData(BaseModel):
    questions: list[ResultQuestionData]


def check_questions_answers(task_block_target: TaskBlock, questions: list[ResultQuestionData]) -> bool:

    task_block_target_questions: list[dict] = json.loads(task_block_target.questions_json)
    print()
    pprint.pprint(task_block_target_questions)

    print()
    pprint.pprint(questions)

    for question_res in questions:
        target_q = task_block_target_questions[question_res.question_uuid]

        try:
            answer = target_q['variants'][question_res.select_variants_content[0]]
        except KeyError:
            return False

        if not answer['is_answer']:
            return False

    return True


router = APIRouter()


@router.get("/all")
async def get_all_task_blocks() -> list[TaskBlockResponse]:

    task_blocks_list = await db_get_all_task_blocks()

    task_blocks_response_list = list(map(
        lambda task_block: TaskBlockResponse.from_task_block(task_block),
        task_blocks_list
    ))

    return task_blocks_response_list


@router.get("/{uuid}")
async def get_task_block(uuid: str) -> TaskBlockResponse:

    return TaskBlockResponse.from_task_block(await db_get_task_block(uuid))


@router.post('/{uuid}/result')
async def check_task_block_result(uuid: str, user: AuthUser, result_data: ResultTaskBlockData) -> bool:

    task_block = await db_get_task_block(uuid)
    res = check_questions_answers(task_block_target=task_block, questions=result_data.questions)

    return res


@router.post("/")
async def create_task_block(user: AuthUser, task_block_data: TaskBlock):

    task_block_data_dict = task_block_data.dict(exclude={'questions'})

    questions_dict = dict()

    for question in task_block_data.questions:
        questions_dict[str(uuid.uuid4())] = question.dict()

    print(json.dumps(questions_dict))

    task_block = TaskBlock(
        uuid=str(uuid.uuid4()),
        questions_json=json.dumps(questions_dict),
        **task_block_data_dict
    )

    pprint.pprint(task_block.dict())

    await db_create_task_block(task_block)
