# AUTOGENERATED FROM 'app/queries/get_worker_by_token.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations

import dataclasses
import datetime
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
class GetWorkerByTokenResult(NoPydanticValidation):
    id: uuid.UUID
    name: str
    photo: str
    birthday: datetime.datetime
    bio: str
    hash: str
    email: str


async def get_worker_by_token(
    executor: edgedb.AsyncIOExecutor,
    *,
    user_id: uuid.UUID,
) -> GetWorkerByTokenResult | None:
    return await executor.query_single(
        """\
        select Worker {id, name, photo, birthday, bio, hash, email}
        filter .tokens.owner.id = <uuid>$user_id
        limit 1\
        """,
        user_id=user_id,
    )
