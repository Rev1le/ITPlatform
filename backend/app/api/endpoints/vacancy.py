from fastapi import APIRouter

from app.deps import AuthEmplayer
from app.core.database import edgedb_client
from app.queries.get_vacancies_async_edgeql import GetVacanciesResult, get_vacancies


class VacancyData():
    pass


router = APIRouter()


@router.get("/all")
async def get_all_vacancies() -> list[GetVacanciesResult]:
    return await get_vacancies(edgedb_client)


@router.post("/")
async def create_vacancy(employer: AuthEmplayer, vacancy_data: VacancyData) -> list[GetVacanciesResult]:
    return await get_vacancies(edgedb_client)
