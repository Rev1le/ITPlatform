import sqlite3

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.api.deps import AuthUser, GetLogger
from app.db.queries.create.create_mentor_async import create_mentor as db_create_mentor
from app.db.queries.get.get_mentor_by_uuid_async import get_mentor_by_uuid_async
from app.db.queries.get.get_all_mentors_async import get_all_mentors as db_get_all_mentors
from app.db import entities

router = APIRouter()


class MentorData(BaseModel):
    skills: list[str]
    salary: float
    resume: str


@router.get("/all")
async def get_all_mentors(logger: GetLogger) -> list[entities.ResponseMentor]:

    #mentors = await get_all_mentors_users_skills()
    mentors = await db_get_all_mentors()
    #logger.log(f"Полученные менторы: {mentors}")
    resp_mentors = list(map(lambda mentor: entities.ResponseMentor(**mentor.dict()), mentors))
    #print(resp_mentors)
    return resp_mentors


@router.post("/")
async def create(logger: GetLogger, user: AuthUser, mentor_data: MentorData) -> str:
    mentor = entities.Mentor(
        user=user,
        salary=mentor_data.salary,
        resume=mentor_data.resume,
        skills=mentor_data.skills
    )

    logger.log(str(mentor))

    try:
        await db_create_mentor(mentor)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=404, detail={"message": "You are already a mentor"})

    return "ok"


@router.get("/{uuid}")
async def get_mentor(uuid: str) -> entities.ResponseMentor:
    mentor = await get_mentor_by_uuid_async(uuid)
    print(mentor.dict())
    return entities.ResponseMentor(**mentor.dict())
