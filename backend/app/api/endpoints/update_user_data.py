from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.api.deps import check_auth_employer_token, check_auth_worker_token
from app.core.database import edgedb_client

import app.queries as db_queries
from db_queries.get_employer_by_token_async_edgeql import GetEmployerByTokenResult
from db_queries.get_worker_by_token_async_edgeql import GetWorkerByTokenResult
from db_queries.update_employer_async_edgeql import update_employer
from db_queries.update_worker_async_edgeql import update_worker

router = APIRouter()


class UpdateDataEmployer(BaseModel):
    description: str | None
    photo: str | None  # Фото ссылкой отправляется



class UpdateDataWorker(BaseModel):
    description: str | None
    photo: str | None
    resume: str | None
    skills: list[str] | None


@router.put("/employer")
async def put_employer(
    employer: Annotated[GetEmployerByTokenResult, Depends(check_auth_employer_token)],
    update_data: UpdateDataEmployer,
):
    await update_employer(
        edgedb_client,
        id=employer.id,
        bio=update_data.description,
        photo=update_data.photo,
    )



@router.put("/worker")
async def put_worker(
    worker: Annotated[GetWorkerByTokenResult, Depends(check_auth_worker_token)],
    update_data: UpdateDataWorker,
):
    await update_worker(
        edgedb_client,
<<<<<<< HEAD
        id=worker.id,
        bio=update_data.description,
        photo=update_data.photo,
        resume=update_data.resume,
        skills=update_data.skills,
    )
=======
        id = worker.id,
        bio = update_data.description,
        photo = update_data.photo,
        resume = update_data.resume,
        skills = update_data.skills
        )
>>>>>>> 78fdfc5626ef83b0013af58cc6d423c5570d4c05
