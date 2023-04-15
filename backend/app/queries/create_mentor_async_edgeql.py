# AUTOGENERATED FROM 'app/queries/create_mentor.edgeql' WITH:
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
class CreateMentorResult(NoPydanticValidation):
    id: uuid.UUID


async def create_mentor(
    executor: edgedb.AsyncIOExecutor,
    *,
    user_id: uuid.UUID,
    skills: list[str],
    salary: float,
    resume: str,
) -> CreateMentorResult:
    return await executor.query_single(
        """\
        insert Mentor {
            employer := (
                select Employer
                filter .id = <uuid>$user_id
            ),
            skills := <array<str>>$skills,
            salary := <float32>$salary,
            resume := <str>$resume
        }\
        """,
        user_id=user_id,
        skills=skills,
        salary=salary,
        resume=resume,
    )