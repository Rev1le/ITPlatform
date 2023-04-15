from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.core.database import edgedb_client
from app.queries.get_task_block_async_edgeql import get_task_block, GetTaskBlockResult
from app.queries.get_task_block_challenges_async_edgeql import get_task_block_challenges, GetTaskBlockChallengesResult
from app.queries.get_task_blocks_preview_async_edgeql import (
    GetTaskBlocksPreviewResult,
    get_task_blocks_preview,
)

router = APIRouter()


@router.get("/all")
async def all_tasks_blocks() -> list[GetTaskBlocksPreviewResult]:
    return await get_task_blocks_preview(edgedb_client)


@router.get("/{id}")
async def task_block_info(id: UUID) -> GetTaskBlockResult:
    result = await get_task_block(edgedb_client, user_id=id)
    if result is None:
        raise HTTPException(status_code=404, detail={"message": "Unknown task block"})
    return result


@router.get("/{id}/challenges")
async def task_block_challenges(id: UUID) -> GetTaskBlockChallengesResult:
    result = await get_task_block_challenges(edgedb_client, task_block_id=id)
    if result is None:
        raise HTTPException(status_code=404, detail={"message": "Unknown task block"})
    return result
