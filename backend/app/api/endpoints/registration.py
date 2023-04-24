import hashlib
import secrets
import sqlite3
from datetime import datetime, timezone

import edgedb
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.database import edgedb_client
from app.queries.create_employer_async_edgeql import create_employer
from app.queries.create_employer_token_async_edgeql import create_employer_token
from app.queries.create_worker_async_edgeql import create_worker
from app.queries.create_worker_token_async_edgeql import create_worker_token
from app.db import db


class Registration(BaseModel):
    email: str
    password: str
    name: str
    birthday: str


class RegistrationAccess(BaseModel):
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
        result = await db.create_employer(db.Employer(
            name=registration_data.name,
            birthday=birthday,
            password_hash=password_hash,
            email=registration_data.email,
            bio=None,
            photo=None
        ))
        print(result)

    except sqlite3.IntegrityError as e:
        print("Create employer error =>", e)
        raise HTTPException(status_code=404, detail={"message": "Invalid login data"})

    auth_token = secrets.token_urlsafe(32)

    #await create_employer_token(edgedb_client, token=auth_token, user_id=employer.id)

    return RegistrationAccess(token=auth_token)


@router.post("/worker")
async def registration_worker(registration_data: Registration) -> RegistrationAccess:
    birthday = datetime.strptime(registration_data.birthday, "%d-%m-%Y").replace(
        tzinfo=timezone.utc
    )

    password_hash = hashlib.sha256(registration_data.password.encode()).hexdigest()

    employer = await create_worker(
        edgedb_client,
        name=registration_data.name,
        birthday=birthday,
        hash=password_hash,
        email=registration_data.email,
    )

    auth_token = secrets.token_urlsafe(32)

    await create_worker_token(edgedb_client, token=auth_token, user_id=employer.id)

    return RegistrationAccess(token=auth_token)
