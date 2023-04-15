from typing import Any, Annotated
import hashlib
import secrets
from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel

from app.core.database import edgedb_client
from app.create_employer_async_edgeql import create_employer
from app.create_worker_async_edgeql import create_worker
from app.queries.create_employer_token_async_edgeql import create_employer_token
from app.queries.create_worker_token_async_edgeql import create_worker_token


class Registration(BaseModel):
    email: str
    password: str
    name: str
    decription: str
    date_of_birth: str
    avatar: Annotated[UploadFile, File()]


class RegistrationAccess(BaseModel):
    token: str


router = APIRouter()


@router.post("/employer")
async def registration_employer(registration_data: Registration):
    
    result = await create_employer(
        edgedb_client, 
        name = registration_data.name,
        birthday = registration_data.date_of_birth,
        hash = hashlib.sha256(registration_data.password).hexdigest(),
        email = registration_data.email
        )

    auth_token = secrets.token_urlsafe(32)

    await create_employer_token(
        edgedb_client, 
        token=auth_token, 
        user_id=employer.id
        )

    return RegistrationAccess(token=auth_token)


@router.post("/worker")
async def registration_worker(registration_data: Registration):
    
    result = await create_worker(
        edgedb_client, 
        name = registration_data.name,
        birthday = registration_data.date_of_birth,
        hash = hashlib.sha256(registration_data.password).hexdigest(),
        email = registration_data.email
        )

    auth_token = secrets.token_urlsafe(32)

    await create_worker_token(
        edgedb_client, 
        token=auth_token, 
        user_id=employer.id
        )

    return RegistrationAccess(token=auth_token)
