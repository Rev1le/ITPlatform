from fastapi import APIRouter

from app.core.database import edgedb_client
from app.queries.get_vacancies_async_edgeql import get_vacancies


router = APIRouter()


@router.get("/")
async def get_all_vacancies():
    return await get_vacancies(edgedb_client)
