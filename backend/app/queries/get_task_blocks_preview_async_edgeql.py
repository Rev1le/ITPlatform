# AUTOGENERATED FROM 'app/queries/get_task_blocks_preview.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations
import dataclasses
import edgedb
import uuid


class NoPydanticValidation:
    @classmethod
    def __get_validators__(cls):
        from pydantic.dataclasses import dataclass as pydantic_dataclass
        pydantic_dataclass(cls)
        cls.__pydantic_model__.__get_validators__ = lambda: []
        return []


@dataclasses.dataclass
class GetTaskBlocksPreviewResult(NoPydanticValidation):
    id: uuid.UUID
    name: str
    difficulty: int
    description: str
    completed_count: int
    is_completed: bool
    is_failed: bool


async def get_task_blocks_preview(
    executor: edgedb.AsyncIOExecutor,
    *,
    user_id: uuid.UUID,
) -> list[GetTaskBlocksPreviewResult]:
    return await executor.query(
        """\
        select TaskBlock {
            id,
            name,
            difficulty,
            description,
            completed_count := count(.completed),
            is_completed := (select <uuid>$user_id in TaskBlock.completed.id),
            is_failed := (select <uuid>$user_id in TaskBlock.failed.id)
        }\
        """,
        user_id=user_id,
    )
