import sqlite3

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.api.deps import AuthUser, GetLogger
from app.db.queries.create_mentor_async import create_mentor
from app.db.queries.create_skill_async import create_skill
from app.db.queries.create_many_mentor_skill_async import create_many_mentor_skill
from app.db.queries.try_create_many_skills_async import try_create_many_skills
from app.db.queries.get_all_mentors_async import get_all_mentors as db_get_all_mentors
from app.db.queries.get_all_mentors_users_skills_async import get_all_mentors_users_skills, MentorUser
from app.db.queries.get_mentor_user_skill_async import get_mentor_user_skill as db_get_mentor
from app.db import entities

router = APIRouter()


class MentorData(BaseModel):
    skills: list[str]
    salary: float
    resume: str


@router.get("/all")
async def get_all_mentors(logger: GetLogger) -> list[MentorUser]:
    #mentors = await db_get_all_mentors()

    mentors = await get_all_mentors_users_skills()
    logger.log(f"Полученные менторы: {mentors}")

    return mentors


@router.post("/")
async def create(logger: GetLogger, user: AuthUser, mentor_data: MentorData) -> str:
    mentor = entities.Mentor(
        uuid=user.uuid,
        salary=mentor_data.salary,
        resume=mentor_data.resume
    )
    logger.log(str(mentor))
    try:
        await create_mentor(mentor)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=404, detail={"message": "You are already a mentor"})

    (getting_skills, creating_skills) = await try_create_many_skills(mentor_data.skills)
    logger.log(str(getting_skills + creating_skills))

    await create_many_mentor_skill(mentor.uuid, getting_skills + creating_skills)

    return "ok"


@router.get("/{uuid}")
async def get_mentor(uuid: str) -> MentorUser:
    return await db_get_mentor(uuid)
