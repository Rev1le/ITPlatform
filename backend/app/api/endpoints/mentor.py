from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel

from app.api.deps import AuthEmplayer
from app.core.database import edgedb_client
from app.queries.create_mentor_async_edgeql import CreateMentorResult, create_mentor
from app.queries.get_mentors_async_edgeql import GetMentorsResult, get_mentors

router = APIRouter()


class MentorData(BaseModel):
    user_id: UUID
    skills: list[str]
    salary: float
    resume: str


@router.get("/all")
async def get_all_mentors() -> list[GetMentorsResult]:
    return await get_mentors(edgedb_client)


@router.post("/create_mentor")
async def create(employer: AuthEmplayer, mentor_data: MentorData) -> CreateMentorResult:
    return await create_mentor(
        edgedb_client,
        user_id=employer.id,
        skills=mentor_data.skills,
        salary=mentor_data.salary,
        resume=mentor_data.resume,
    )
