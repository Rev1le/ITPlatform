import secrets
import uuid
from typing import Annotated
from uuid import UUID, uuid4

import sqlalchemy
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.api.deps import AuthUser
from app.db import Skill, database, vacancy_skills_table, vacancies_table, entities
from app.db.entities import Vacancy
from app.db.queries.create_many_skills_async import create_many_skills
from app.db.queries.create_vacancy_async import create_vacancy as db_create_vacancy
from app.db.queries.get_all_vacancies_async import get_all_vacancies as db_get_all_vacancies
from app.db.queries.get_vacancy_by_uuid_async import get_vacancy_by_uuid_async
from app.db.entities import skills_table


class VacancyData(BaseModel):
    name: str
    description: str
    skills: list[str]
    company: str
    salary: float | None
    #required_task_block_ids: list[UUID] | None


router = APIRouter()


@router.get("/all")
async def get_all_vacancies() -> list[entities.Vacancy]:
    return await db_get_all_vacancies()


@router.post("/")
async def create_vacancy(user: AuthUser, vacancy_data: VacancyData) -> Vacancy:
    vacancy = Vacancy(
        uuid=str(uuid.uuid4()),
        author_uuid=user.uuid,
        **vacancy_data.dict()
    )

    await db_create_vacancy(vacancy)
    return vacancy


@router.get("/{uuid}")
async def vacancy(uuid: UUID) -> Vacancy:
    return await get_vacancy_by_uuid_async(str(uuid))


