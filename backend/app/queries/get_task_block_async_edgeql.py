# AUTOGENERATED FROM 'app/queries/get_task_block.edgeql' WITH:
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
class GetTaskBlockResult(NoPydanticValidation):
    id: uuid.UUID
    name: str
    difficulty: int
    description: str
    completed_count: int


async def get_task_block(
    executor: edgedb.AsyncIOExecutor,
    *,
    user_id: uuid.UUID,
) -> GetTaskBlockResult | None:
    return await executor.query_single(
        """\
        select TaskBlock {
            id,
            name,
            difficulty,
            description,
            completed_count := count(.completed)
        }
        filter .id = <uuid>$user_id\
        """,
        user_id=user_id,
    )
