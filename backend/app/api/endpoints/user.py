import uuid
import hashlib
import sqlite3
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


from app.api.deps import GetLogger
from app import db
from app.api.deps import AuthUser
from app.db import entities
from app.db.queries.create.create_user_async import create_user
from app.db.queries.create.create_auth_token_async import create_auth_token
from app.db.queries.get.get_user_by_uuid_async import get_user_by_uuid_async
from app.db.queries.get.get_user_by_email_password_hash_async import get_user_by_email_password_hash


class Registration(BaseModel):
    email: str
    password: str
    name: str
    birthday: str


class RegistrationAccess(BaseModel):
    name: str
    token: str


class AuthData(BaseModel):
    email: str
    password: str


class LoginAccess(BaseModel):
    name: str
    token: str


router = APIRouter()


@router.get("/me")
async def get_user_by_token(user: AuthUser) -> entities.ResponseUser:
    return entities.ResponseUser(**user.dict())


@router.get("/{uuid}")
async def get_user_by_token(user: AuthUser, uuid: str) -> entities.ResponseUser:
    user_from_uuid = await get_user_by_uuid_async(uuid)
    return entities.ResponseUser(**user_from_uuid.dict())


@router.post("/reg")
async def registration_user(registration_data: Registration, logger: GetLogger) -> RegistrationAccess:
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
        logger.log(f"Create user error => {e}")
        raise HTTPException(status_code=404, detail={"message": "Invalid registration data"})

    token_data = await create_auth_token(user.uuid)

    return RegistrationAccess(
        token=token_data.token,
        name=user.name
    )


@router.post("/auth")
async def auth_user(auth_data: AuthData) -> LoginAccess:

    print(auth_data)

    password_hash = hashlib\
        .sha256(auth_data.password.encode())\
        .hexdigest()

    employer = await get_user_by_email_password_hash(
        email=auth_data.email,
        password_hash=password_hash
    )
    print("Полученный user => ", employer)

    if employer is None:
        raise HTTPException(
            status_code=404,
            detail={"message": "Invalid login data"}
        )

    token_data = await create_auth_token(employer.uuid)

    return LoginAccess(token=token_data.token, name=employer.name)