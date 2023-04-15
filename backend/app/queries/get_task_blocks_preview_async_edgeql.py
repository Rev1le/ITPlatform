# AUTOGENERATED FROM 'app/queries/get_task_blocks_preview.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations

import dataclasses
import uuid

import edgedb


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


async def get_task_blocks_preview(
    executor: edgedb.AsyncIOExecutor,
) -> list[GetTaskBlocksPreviewResult]:
    return await executor.query(
        """\
        select TaskBlock {
            id,
            name,
            difficulty,
            description,
            completed_count := count(.completed)
        }\
        """,
    )
