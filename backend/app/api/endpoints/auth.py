import datetime
import hashlib
import secrets
import uuid

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.db.queries.get_user_by_email_password_hash_async import get_user_by_email_password_hash
from app.db.queries.create_auth_token_async import create_auth_token
from app import db


class AuthData(BaseModel):
    email: str
    password: str


class LoginAccess(BaseModel):
    name: str
    token: str


router = APIRouter()


# @router.get("/")
# async def test():
#     # await app.db.users.create_user(app.db.User(
#     #     uuid="TestUUId",
#     #     email="roman@mail",
#     #     password_hash="2002",
#     #     name="Roman",
#     #     birthday=datetime.datetime(2022, 11, 3)
#     # ))
#     return await app.db.users.append_skills_to_job_applicant(
#         [
#             app.db.Skill(uuid=str(uuid.uuid4()), name="Rust"),
#             app.db.Skill(uuid=str(uuid.uuid4()), name="Python")
#         ]
#     )
#     #return await app.db.users.get_user(email="roman@mail", password_hash="2002")

@router.post("/")
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
