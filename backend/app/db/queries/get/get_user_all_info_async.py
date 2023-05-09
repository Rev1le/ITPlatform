from datetime import datetime

from pydantic import BaseModel
import sqlalchemy
from app.db import entities, mentors_table, database


class MentorInfo(BaseModel):
    salary: float
    resume: str | None
    skills: list[str]


class JobApplicantInfo(BaseModel):
    resume: str | None
    skills: list[str]


class UserInfo(BaseModel):
    uuid: str
    email: str
    password_hash: str
    name: str
    birthday: datetime.date
    bio: str | None
    photo: str | None
    mentor: MentorInfo | None
    job_applicant: JobApplicantInfo | None


async def get_user_all_info(uuid: str) -> UserInfo:
    pass