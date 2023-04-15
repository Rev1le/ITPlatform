from pydantic import BaseModel
from fastapi import APIRouter

from app.api.deps import AuthEmplayer
from app.core.database import edgedb_client
from app.queries.get_vacancies_async_edgeql import GetVacanciesResult, get_vacancies
from app.queries.create_vacancy_async_edgeql import CreateVacancyResult, create_vacancy as db_create_vacancy


class VacancyData(BaseModel):
    name: str
    about: str
    skills: list[str]
    company: str
    salary: float | None # If None the salary = 


router = APIRouter()


@router.get("/all")
async def get_all_vacancies() -> list[GetVacanciesResult]:
    return await get_vacancies(edgedb_client)


@router.post("/")
async def create_vacancy(employer: AuthEmplayer, vacancy_data: VacancyData) -> CreateVacancyResult:
    
    return await db_create_vacancy(
        edgedb_client,
        name = vacancy_data.name,
        about = vacancy_data.about,
        skills = vacancy_data.skills,
        company = vacancy_data.company,
        salary = vacancy_data.salary,
    )
