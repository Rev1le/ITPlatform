from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.api.deps import AuthEmplayer, check_auth_employer_token
from app.core.database import edgedb_client
from app.queries.create_mentor_async_edgeql import CreateMentorResult, create_mentor
from app.queries.get_employer_by_token_async_edgeql import GetEmployerByTokenResult
from app.queries.get_mentors_async_edgeql import GetMentorsResult, get_mentors

router = APIRouter()


class MentorData(BaseModel):
    skills: list[str]
    salary: float
    resume: str


@router.get("/all")
async def get_all_mentors() -> list[GetMentorsResult]:
    return await get_mentors(edgedb_client)


@router.post("/")
async def create(employer: Annotated[GetEmployerByTokenResult, Depends(check_auth_employer_token)],
                 mentor_data: MentorData) -> str:

    print(employer.mentor[0])

    try:
        await create_mentor(
            edgedb_client,
            user_id=employer.id,
            skills=mentor_data.skills,
            salary=mentor_data.salary,
            resume=mentor_data.resume
        )

    except:
        raise HTTPException(status_code=404, detail={"message": "Invalid mentor data"})

    return "ok"
