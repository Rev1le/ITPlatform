import hashlib
import secrets

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.db import db


class AuthData(BaseModel):
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str


class LoginAccess(BaseModel):
    name: str
    token: str


router = APIRouter()


@router.post("/")
async def auth_user(auth_data: AuthData) -> LoginAccess:

    job_applicant_login_access = await auth_job_applicant(auth_data=auth_data)
    if job_applicant_login_access is not None:
        return job_applicant_login_access

    employer_login_access = await auth_employer(auth_data=auth_data)
    if employer_login_access is not None:
        return employer_login_access

    raise HTTPException(status_code=404, detail={"message": "Invalid login data"})


async def auth_employer(auth_data: AuthData) -> LoginAccess | None:

    password_hash = hashlib\
        .sha256(auth_data.password.encode())\
        .hexdigest()

    employer = await db.get_employer_by_email_hash(
        email=auth_data.email,
        password_hash=password_hash
    )
    print("Полученный employer => ", employer)

    if employer is None:
        return None

    token_data = await db.create_employer_auth_token(employer.uuid)

    return LoginAccess(token=token_data.token, name=employer.name)


async def auth_job_applicant(auth_data: AuthData) -> LoginAccess | None:

    password_hash = hashlib \
        .sha256(auth_data.password.encode()) \
        .hexdigest()

    job_applicant = await db.get_job_applicant_by_email_hash(
        email=auth_data.email,
        password_hash=password_hash
    )
    print("Полученный job_applicant => ", job_applicant)

    if job_applicant is None:
        return None

    auth_token = secrets.token_urlsafe(32)

    await db.create_job_applicant_auth_token(job_applicant.uuid)
    return LoginAccess(token=auth_token, name=job_applicant.name)
