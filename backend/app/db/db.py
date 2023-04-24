import secrets
import uuid
from typing import List

import datetime
import databases
import sqlalchemy
from pydantic import BaseModel

from app.db.entities import employers_table, metadata, Employer, AuthToken, tokens_table

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
        uuid=str(uuid.uuid4()),
        name=employer.name,
        birthday=employer.birthday,
        password_hash=employer.password_hash,
        email=employer.email,
        bio=employer.bio,
        photo=employer.photo
    )
    last_record_id = await database.execute(query)
    #print("last_record_id", last_record_id)
    return {**employer.dict()}


async def get_employer_by_email_hash(email: str, password_hash: str):
    query = sqlalchemy\
        .select(employers_table)\
        .where(employers_table.c.email == email)\
        .where(employers_table.c.password_hash == password_hash)

    #print('Запрос получения employer => ',query)

    return await database.fetch_one(
        query,
        #values={"email": email, "password_hash": password_hash}
    )


async def create_employer_auth_token(employer_uuid: str):

    auth_token = secrets.token_urlsafe(32)

    query = tokens_table\
        .insert()\
        .values(
            token=auth_token,
            owner_uuid=employer_uuid
        )

    last_record_id = await database.execute(query)
    #print("last_record_id", last_record_id)
    return AuthToken(token=auth_token, owner_uuid=employer_uuid)
