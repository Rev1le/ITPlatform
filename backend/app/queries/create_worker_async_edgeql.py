# AUTOGENERATED FROM 'app/queries/create_worker.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations
import dataclasses
import datetime
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
class CreateWorkerResult(NoPydanticValidation):
    id: uuid.UUID


async def create_worker(
    executor: edgedb.AsyncIOExecutor,
    *,
    name: str,
    birthday: datetime.datetime,
    hash: str,
    email: str,
) -> CreateWorkerResult:
    return await executor.query_single(
        """\
        insert Worker {
            name := <str>$name,
            birthday := <datetime>$birthday,
            hash := <str>$hash,
            email := <str>$email
        }\
        """,
        name=name,
        birthday=birthday,
        hash=hash,
        email=email,
    )
