from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter()


class UpdateDataEmployer(BaseModel):
    description: str | None
    photo: str | None  # Фото ссылкой отправляется


class UpdateDataWorker(BaseModel):
    description: str | None
    photo: str | None
    resume: str | None
    skills: list[str] | None


# @router.put("/employer")
# async def put_employer(
#     employer: Annotated[GetEmployerByTokenResult, Depends(check_auth_employer_token)],
#     update_data: UpdateDataEmployer,
# ):
#     await update_employer(
#         edgedb_client,
#         id=employer.id,
#         bio=update_data.description,
#         photo=update_data.photo,
#     )
#
#
# @router.put("/worker")
# async def put_worker(
#     worker: Annotated[GetWorkerByTokenResult, Depends(check_auth_job_applicant_token)],
#     update_data: UpdateDataWorker,
# ):
#     await update_worker(
#         edgedb_client,
#         id=worker.id,
#         bio=update_data.description,
#         photo=update_data.photo,
#         resume=update_data.resume,
#         skills=update_data.skills,
#     )
