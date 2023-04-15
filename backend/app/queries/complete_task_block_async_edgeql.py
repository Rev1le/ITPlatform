# AUTOGENERATED FROM 'app/queries/complete_task_block.edgeql' WITH:
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
class CompleteTaskBlockResult(NoPydanticValidation):
    id: uuid.UUID


async def complete_task_block(
    executor: edgedb.AsyncIOExecutor,
    *,
    task_block_id: uuid.UUID,
    user_id: uuid.UUID,
) -> CompleteTaskBlockResult | None:
    return await executor.query_single(
        """\
        update TaskBlock
        filter .id = <uuid>$task_block_id
        set {
            completed := distinct(.completed union (
                select Worker filter .id = <uuid>$user_id
            ))
        }\
        """,
        task_block_id=task_block_id,
        user_id=user_id,
    )
