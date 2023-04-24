import hashlib
import secrets
import sqlite3
import uuid
from datetime import datetime, timezone

import edgedb
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.database import edgedb_client
from app.queries.create_worker_async_edgeql import create_worker
from app.queries.create_worker_token_async_edgeql import create_worker_token
from app.db import db


class Registration(BaseModel):
    email: str
    password: str
    name: str
    birthday: str


class RegistrationAccess(BaseModel):
    name: str
    token: str


router = APIRouter()


@router.post("/employer")
async def registration_employer(registration_data: Registration) -> RegistrationAccess:

    birthday = datetime\
        .strptime(registration_data.birthday, "%d-%m-%Y")\
        .replace(tzinfo=timezone.utc)
    password_hash = hashlib\
        .sha256(registration_data.password.encode())\
        .hexdigest()

    try:
        created_employer = await db.create_employer(db.Employer(
            uuid=str(uuid.uuid4()),
            name=registration_data.name,
            birthday=birthday,
            password_hash=password_hash,
            email=registration_data.email,
            bio=None,
            photo=None
        ))
        print(created_employer)

    except sqlite3.IntegrityError as e:
        print("Create employer error =>", e)
        raise HTTPException(status_code=404, detail={"message": "Invalid login data"})

    auth_token = secrets.token_urlsafe(32)

    token_data = await db.create_employer_auth_token(created_employer.uuid)

    return RegistrationAccess(token=token_data.token, name=created_employer.name)


@router.post("/job_applicant")
async def registration_worker(registration_data: Registration) -> RegistrationAccess:
    birthday = datetime\
        .strptime(registration_data.birthday, "%d-%m-%Y")\
        .replace(tzinfo=timezone.utc)

    password_hash = hashlib\
        .sha256(registration_data.password.encode())\
        .hexdigest()

    try:
        created_job_applicant = await db.create_job_applicant(
            db.JobApplicant(
                uuid=str(uuid.uuid4()),
                name=registration_data.name,
                birthday=birthday,
                password_hash=password_hash,
                email=registration_data.email,
                bio=None,
                photo=None,
                resume=None,
                skills=[]
            )
        )
        print(created_job_applicant)

    except sqlite3.IntegrityError as e:
        print("Create employer error =>", e)
        raise HTTPException(status_code=404, detail={"message": "Invalid login data"})

    token_data = await db.create_job_applicant_auth_token(created_job_applicant.uuid)

    return RegistrationAccess(token=token_data.token, name=created_job_applicant.name)
