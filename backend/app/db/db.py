import secrets
import uuid
from typing import List

import datetime
import databases
import sqlalchemy
from pydantic import BaseModel

from app.db.entities import *

# SQLAlchemy specific code, as with any other app
DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


async def startup():
    await database.connect()


async def shutdown():
    await database.disconnect()


async def get_all_employers() -> List[object]:
    query = employers_table.select()
    return await database.fetch_all(query)


async def create_employer(employer: Employer):
    query = employers_table.insert().values(
        uuid=employer.uuid,
        name=employer.name,
        birthday=employer.birthday,
        password_hash=employer.password_hash,
        email=employer.email,
        bio=employer.bio,
        photo=employer.photo
    )
    await database.execute(query)
    return employer


async def get_employer_by_email_hash(email: str, password_hash: str):
    query = sqlalchemy \
        .select(employers_table) \
        .where(employers_table.c.email == email) \
        .where(employers_table.c.password_hash == password_hash)

    # print('Запрос получения employer => ',query)
    return await database.fetch_one(
        query,
        # values={"email": email, "password_hash": password_hash}
    )


async def create_employer_auth_token(employer_uuid: str):
    auth_token = secrets.token_urlsafe(32)

    query = tokens_table \
        .insert() \
        .values(
        token=auth_token,
        owner_uuid=employer_uuid
    )

    await database.execute(query)
    return AuthToken(token=auth_token, owner_uuid=employer_uuid)


async def create_skill(skill_name: str):
    query = skills_table \
        .insert() \
        .values(name=skill_name)

    await database.execute(query)


async def create_job_applicant(job_applicant: JobApplicant):
    query = job_applicant_table\
        .insert()\
        .values(
            uuid=str(uuid.uuid4()),
            name=job_applicant.name,
            birthday=job_applicant.birthday,
            password_hash=job_applicant.password_hash,
            email=job_applicant.email,
            bio=job_applicant.bio,
            photo=job_applicant.photo
    )

    await database.execute(query)
    return job_applicant


async def get_job_applicant_by_email_hash(email: str, password_hash: str):
    query = sqlalchemy \
        .select(job_applicant_table) \
        .where(job_applicant_table.c.email == email) \
        .where(job_applicant_table.c.password_hash == password_hash)

    # print('Запрос получения job_applicant => ',query)
    return await database.fetch_one(
        query,
        # values={"email": email, "password_hash": password_hash}
    )


async def create_job_applicant_auth_token(job_applicant_uuid: str):
    auth_token = secrets.token_urlsafe(32)

    query = tokens_table \
        .insert() \
        .values(
        token=auth_token,
        owner_uuid=job_applicant_uuid
    )

    await database.execute(query)
    return AuthToken(token=auth_token, owner_uuid=job_applicant_uuid)