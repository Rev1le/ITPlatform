import hashlib
import secrets

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.database import edgedb_client
from app.queries.create_employer_token_async_edgeql import create_employer_token
from app.queries.create_worker_token_async_edgeql import create_worker_token
from app.queries.get_employer_by_hash_async_edgeql import get_employer_by_hash
from app.queries.get_worker_by_hash_async_edgeql import get_worker_by_hash


class Login(BaseModel):
    email: str
    password: str


class LoginAccess(BaseModel):
    token: str


router = APIRouter()


@router.post("/employer")
async def auth_employer(login: Login) -> LoginAccess:
    password_hash = hashlib.sha256(login.password.encode()).hexdigest()

    employer = await get_employer_by_hash(
        edgedb_client, hash=password_hash, email=login.email
    )

    if employer is None:
        raise HTTPException(status_code=404, detail={"message": "Invalid login data"})

    auth_token = secrets.token_urlsafe(32)

    await create_employer_token(edgedb_client, token=auth_token, user_id=employer.id)

    return LoginAccess(token=auth_token)


@router.post("/worker")
async def auth_worker(login: Login) -> LoginAccess:
    password_hash = hashlib.sha256(login.password).hexdigest()

    worker = await get_worker_by_hash(
        edgedb_client, hash=password_hash, email=login.email
    )

    if worker is None:
        raise HTTPException(status_code=404, detail={"message": "Invalid login data"})

    auth_token = secrets.token_urlsafe(32)

    await create_worker_token(edgedb_client, token=auth_token, user_id=worker.id)

    return LoginAccess(token=auth_token)
