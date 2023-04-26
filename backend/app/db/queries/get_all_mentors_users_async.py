import datetime

import sqlalchemy
from pydantic import BaseModel
from app.db import entities, mentors_table, database, users_table


class MentorUser(BaseModel):
    uuid: str
    name: str
    salary: float
    resume: str | None
    birthday: datetime.date
    bio: str | None
    photo: str | None


async def get_all_mentors_users() -> list[MentorUser]:
    query = sqlalchemy\
        .select(
            users_table.c.name,
            users_table.c.birthday,
            users_table.c.bio,
            users_table.c.photo,
            mentors_table.c.uuid,
            mentors_table.c.salary,
            mentors_table.c.resume
        )\
        .where(users_table.c.uuid == mentors_table.c.uuid)

    result_rows = await database.fetch_all(query)

    return list(map(
        lambda row: MentorUser.parse_obj(dict(row)),
        result_rows
    ))