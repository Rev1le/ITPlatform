import uuid
import sqlite3

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.api.deps import AuthUser
from app import db
from app.db.queries.create.create_job_applicant_async import create_job_applicant
from app.db.queries.create.create_many_skills_async import create_many_skills
from app.db.queries.create.create_many_job_applicant_skill_async import create_many_job_applicant_skill


class RegistrationJobApplicant(BaseModel):
    resume: str | None
    skills: list[str] | None


router = APIRouter()


@router.post("/job_applicant")
async def registration_worker(registration_data: RegistrationJobApplicant, user: AuthUser):

    try:
        await create_job_applicant(
            db.JobApplicant(
                resume=registration_data.resume,
                uuid=user.uuid
            )
        )

        skills_list = list(
            map(
                lambda skill_name: db.Skill(
                    uuid=str(uuid.uuid4()),
                    name=skill_name
                ),
                registration_data.skills
            )
        )

        await create_many_skills(skills_list)
        await create_many_job_applicant_skill(user.uuid, skills_list)

    except sqlite3.IntegrityError as e:
        print("Create job applicant error =>", e)
        raise HTTPException(status_code=404, detail={"message": "Invalid login data"})