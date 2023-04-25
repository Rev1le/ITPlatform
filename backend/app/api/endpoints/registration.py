import hashlib
import secrets
import sqlite3
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.api.deps import AuthUser
from app.db.queries.create_user_async import create_user
from app.db.queries.create_auth_token_async import create_auth_token
from app.db.queries.create_job_applicant_async import create_job_applicant
from app.db.queries.create_many_skills_async import create_many_skills
from app.db.queries.create_many_job_applicant_skill_async import create_many_job_applicant_skill
from app import db


class Registration(BaseModel):
    email: str
    password: str
    name: str
    birthday: str


class RegistrationEmployer(BaseModel):
    ...


class RegistrationJobApplicant(BaseModel):
    resume: str | None
    skills: list[str] | None


class RegistrationAccess(BaseModel):
    name: str
    token: str


router = APIRouter()


@router.post("/user")
async def registration_user(registration_data: Registration) -> RegistrationAccess:
    birthday = datetime\
        .strptime(registration_data.birthday, "%d-%m-%Y")\
        .replace(tzinfo=timezone.utc)

    password_hash = hashlib\
        .sha256(registration_data.password.encode())\
        .hexdigest()

    user = db.User(
        uuid=str(uuid.uuid4()),
        name=registration_data.name,
        birthday=birthday,
        password_hash=password_hash,
        email=registration_data.email,
        bio=None,
        photo=None
    )

    try:
        created_user = await create_user(user)
        print(created_user)

    except sqlite3.IntegrityError as e:
        print("Create user error =>", e)
        raise HTTPException(status_code=404, detail={"message": "Invalid registration data"})

    token_data = await create_auth_token(user.uuid)

    return RegistrationAccess(
        token=token_data.token,
        name=user.name
    )


# @router.post("/employer")
# async def registration_employer(registration_employer_data: Registration) -> RegistrationAccess:
#
#     birthday = datetime\
#         .strptime(registration_data.birthday, "%d-%m-%Y")\
#         .replace(tzinfo=timezone.utc)
#     password_hash = hashlib\
#         .sha256(registration_data.password.encode())\
#         .hexdigest()
#
#     try:
#         created_employer = await db.create_employer(db.Employer(
#             uuid=str(uuid.uuid4()),
#             name=registration_data.name,
#             birthday=birthday,
#             password_hash=password_hash,
#             email=registration_data.email,
#             bio=None,
#             photo=None
#         ))
#         print(created_employer)
#
#     except sqlite3.IntegrityError as e:
#         print("Create employer with error =>", e)
#         raise HTTPException(status_code=404, detail={"message": "Invalid login data"})
#
#     auth_token = secrets.token_urlsafe(32)
#
#     token_data = await db.create_employer_auth_token(created_employer.uuid)
#
#     return RegistrationAccess(token=token_data.token, name=created_employer.name)


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
