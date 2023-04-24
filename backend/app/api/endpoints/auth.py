import hashlib
import secrets

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.database import edgedb_client
from app.queries.create_employer_token_async_edgeql import create_employer_token
from app.queries.create_worker_token_async_edgeql import create_worker_token
from app.queries.get_employer_by_hash_async_edgeql import get_employer_by_hash, GetEmployerByHashResult
from app.queries.get_worker_by_hash_async_edgeql import get_worker_by_hash, GetWorkerByHashResult
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

    # worker_login_access = await auth_worker(password_hash=password_hash, auth_data=auth_data)
    # if worker_login_access is not None:
    #     return worker_login_access
    #
    employer_login_access = await auth_employer(auth_data=auth_data)
    print('Employer token data:', employer_login_access)
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


async def auth_worker(password_hash: str, auth_data: AuthData) -> LoginAccess | None:

    worker = await get_worker_by_hash(
        edgedb_client, hash=password_hash, email=auth_data.email
    )

    if worker is None:
        return None

    auth_token = secrets.token_urlsafe(32)

    await create_worker_token(edgedb_client, token=auth_token, user_id=worker.id)
    return LoginAccess(token=auth_token, name=worker.name)
