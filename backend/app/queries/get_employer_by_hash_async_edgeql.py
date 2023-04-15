# AUTOGENERATED FROM 'app/queries/get_employer_by_hash.edgeql' WITH:
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
class GetEmployerByHashResult(NoPydanticValidation):
    id: uuid.UUID
    name: str
    photo: str
    birthday: datetime.datetime
    bio: str
    hash: str
    email: str


async def get_employer_by_hash(
    executor: edgedb.AsyncIOExecutor,
    *,
    hash: str,
) -> GetEmployerByHashResult | None:
    return await executor.query_single(
        """\
        select Employer {id, name, photo, birthday, bio, hash, email}
        filter Employer.hash = <str>$hash
        limit 1\
        """,
        hash=hash,
    )
