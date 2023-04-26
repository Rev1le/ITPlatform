import sqlalchemy
from pydantic import BaseModel
from app.db import entities, mentors_table, database, users_table
from app.db.queries.get_all_mentors_users_async import MentorUser


async def get_mentor(uuid: str):
    query = sqlalchemy \
        .select(
            users_table.c.name,
            users_table.c.birthday,
            users_table.c.bio,
            users_table.c.photo,
            mentors_table.c.uuid,
            mentors_table.c.salary,
            mentors_table.c.resume
        )\
        .where(mentors_table.c.uuid == uuid)\
        .where(users_table.c.uuid == mentors_table.c.uuid)

    result_row = await database.fetch_one(query)

    return MentorUser.parse_obj(dict(result_row))