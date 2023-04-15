from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.api.deps import AuthEmplayer, check_auth_worker_token
from app.core.database import edgedb_client
from app.queries.create_vacancy_async_edgeql import CreateVacancyResult
from app.queries.create_vacancy_async_edgeql import create_vacancy as db_create_vacancy
from app.queries.get_vacancies_async_edgeql import GetVacanciesResult, get_vacancies
from app.queries.get_vacancy_async_edgeql import GetVacancyResult, get_vacancy
from app.queries.get_worker_by_token_async_edgeql import GetWorkerByTokenResult


class VacancyData(BaseModel):
    name: str
    about: str
    skills: list[str]
    company: str
    salary: float | None  # If None the salary =
    required_task_block_ids: list[UUID]


router = APIRouter()


@router.get("/all")
async def get_all_vacancies() -> list[GetVacanciesResult]:
    return await get_vacancies(edgedb_client)


@router.post("/")
async def create_vacancy(
    employer: AuthEmplayer, vacancy_data: VacancyData
) -> CreateVacancyResult:
    return await db_create_vacancy(
        edgedb_client,
        employer_id=employer.id,
        name=vacancy_data.name,
        about=vacancy_data.about,
        skills=vacancy_data.skills,
        company=vacancy_data.company,
        salary=vacancy_data.salary,
        required_task_block_ids=vacancy_data.required_task_block_ids,
    )


@router.get("/{id}")
async def vacancy(
    id: UUID,
    worker: Annotated[GetWorkerByTokenResult, Depends(check_auth_worker_token)],
) -> GetVacancyResult:
    result = await get_vacancy(edgedb_client, user_id=worker.id, vacancy_id=id)
    if result is None:
        raise HTTPException(status_code=404, detail={"message": "Unknown vacancy"})
    return result
