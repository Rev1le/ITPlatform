import secrets
from typing import Annotated
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

class VacancyData(BaseModel):
    id: str
    name: str
    description: str
    skills: list[str]
    company: str
    salary: float | None  # If None the salary =
    required_task_block_ids: list[UUID]


router = APIRouter()


vacancies_list = [
        VacancyData(
            id=secrets.token_urlsafe(32),
            name="Rust",
            description="Test_vacancy",
            skills=["Rust", "DevOps"],
            company="Sber",
            salary=0,
            required_task_block_ids=[uuid4(), uuid4()]
        ),
        VacancyData(id=secrets.token_urlsafe(32), name="Python", description="Test_vacancy2", skills=["Python", "SQL", "pip"], company="Sber", salary=8000, required_task_block_ids = []),
    ]

# @router.get("/all")
# async def get_all_vacancies() -> list[VacancyData]:
#     return vacancies_list
#     #return await get_vacancies(edgedb_client)
#
#
# @router.post("/")
# async def create_vacancy(
#     employer: Annotated[GetEmployerByTokenResult, Depends(check_auth_employer_token)], vacancy_data: VacancyData
# ) -> CreateVacancyResult:
#     return await db_create_vacancy(
#         edgedb_client,
#         employer_id=employer.id,
#         name=vacancy_data.name,
#         description=vacancy_data.about,
#         skills=vacancy_data.skills,
#         company=vacancy_data.company,
#         salary=vacancy_data.salary,
#         required_task_block_ids=vacancy_data.required_task_block_ids,
#     )
#
# """
# @router.get("/{id}")
# async def vacancy(
#     id: UUID,
#     worker: Annotated[GetWorkerByTokenResult, Depends(check_auth_worker_token)],
# ) -> VacancyData:
#     return vacancies_list[0]
#     # result = await get_vacancy(edgedb_client, user_id=worker.id, vacancy_id=id)
#     # if result is None:
#     #     raise HTTPException(status_code=404, detail={"message": "Unknown vacancy"})
#     # return result
# """
#
# @router.get("/{id}")
# async def vacancy(id: str) -> VacancyData:
#     return vacancies_list[0]
