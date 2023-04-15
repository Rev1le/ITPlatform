from fastapi import APIRouter

from app.core.database import edgedb_client
from app.queries.get_task_blocks_preview_async_edgeql import (
    GetTaskBlocksPreviewResult,
    get_task_blocks_preview,
)

router = APIRouter()


@router.get("/all")
async def get_all_tasks_blocks() -> list[GetTaskBlocksPreviewResult]:
    return await get_task_blocks_preview(edgedb_client)
