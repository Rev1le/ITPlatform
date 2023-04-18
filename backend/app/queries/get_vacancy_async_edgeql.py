# AUTOGENERATED FROM 'app/queries/get_vacancy.edgeql' WITH:
#     $ python.exe -m edgedb.codegen


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
class GetVacancyResult(NoPydanticValidation):
    id: uuid.UUID
    name: str
    description: str
    skills: list[str]
    company: str
    salary: str
    author_id: uuid.UUID
    required_task_blocks: list[GetVacancyResultRequiredTaskBlocksItem]


@dataclasses.dataclass
class GetVacancyResultRequiredTaskBlocksItem(NoPydanticValidation):
    id: uuid.UUID
    name: str
    difficulty: int
    description: str
    is_completed: bool
    is_failed: bool


async def get_vacancy(
    executor: edgedb.AsyncIOExecutor,
    *,
    user_id: uuid.UUID,
    vacancy_id: uuid.UUID,
) -> GetVacancyResult | None:
    return await executor.query_single(
        """\
        select Vacancy {
            name,
            description,
            skills,
            company,
            salary,
            author_id := .author.id,
            required_task_blocks: {
                id,
                name,
                difficulty,
                description,
                is_completed := (select <uuid>$user_id in TaskBlock.completed.id),
                is_failed := (select <uuid>$user_id in TaskBlock.failed.id)
            }
        }
        filter .id = <uuid>$vacancy_id\
        """,
        user_id=user_id,
        vacancy_id=vacancy_id,
    )
