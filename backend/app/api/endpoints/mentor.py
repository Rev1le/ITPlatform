from fastapi import APIRouter

from app.core.database import edgedb_client
from app.api.deps import AuthEmplayer
from app.queries.get_mentors_async_edgeql import GetMentorsResult, get_mentors
from app.queries.create_mentors_async_edgeql import CreateMentorsResult, create_mentor as db_create_mentor

router = APIRouter()


class MentorData():
    user_id: uuid.UUID,
    skills: list[str],
    salary: float,
    resume: str,


@router.get("/all")
async def get_all_mentors() -> list[GetMentorsResult]:
    return await get_mentors(edgedb_client)


@router.post("/create_mentor")
async def create_mentor(
    employer: AuthEmplayer, 
    mentor_data: MentorData
    ) -> CreateMentorsResult:
    
    return await db_create_mentor(
        edgedb_client, 
        user_id = employer.id,
        skills = mentor_data.skills,
        salary = mentor_data.salary,
        resume = mentor_data.resume
        )
