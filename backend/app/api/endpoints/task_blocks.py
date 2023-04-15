from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.api.deps import check_auth_worker_token
from app.core.database import edgedb_client
from app.queries.get_task_block_async_edgeql import GetTaskBlockResult, get_task_block
from app.queries.get_task_block_challenges_async_edgeql import (
    GetTaskBlockChallengesResult,
    get_task_block_challenges,
)
from app.queries.get_task_blocks_preview_async_edgeql import (
    GetTaskBlocksPreviewResult,
    get_task_blocks_preview,
)
from app.queries.get_worker_by_token_async_edgeql import GetWorkerByTokenResult


class Question(BaseModel):
    id: UUID
    answer: str


class Code(BaseModel):
    id: UUID
    lang: str
    answer: str


class Answers(BaseModel):
    questions: list[Question]
    codes: list[Code]


router = APIRouter()


@router.get("/all")
async def all_tasks_blocks() -> list[GetTaskBlocksPreviewResult]:
    return await get_task_blocks_preview(edgedb_client)


@router.get("/{id}")
async def task_block_info(
    id: UUID,
    worker: Annotated[GetWorkerByTokenResult, Depends(check_auth_worker_token)],
) -> GetTaskBlockResult:
    result = await get_task_block(edgedb_client, user_id=worker.id, task_block_id=id)
    if result is None:
        raise HTTPException(status_code=404, detail={"message": "Unknown task block"})
    return result


@router.get("/{id}/challenges")
async def task_block_challenges(
    id: UUID,
    worker: Annotated[GetWorkerByTokenResult, Depends(check_auth_worker_token)],
) -> GetTaskBlockChallengesResult:
    result = await get_task_block_challenges(edgedb_client, task_block_id=id)
    if result is None:
        raise HTTPException(status_code=404, detail={"message": "Unknown task block"})
    return result


@router.post("/{id}")
async def send_answers(answers: Answers):
    pass
