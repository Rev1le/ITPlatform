import sqlalchemy
from app.db import entities, users_table, database


async def get_user_by_uuid_async(user_uuid: str) -> entities.User:
    query = sqlalchemy\
        .select(users_table)\
        .where(users_table.c.uuid == user_uuid)
    result_row = await database.fetch_one(query=query)

    return entities.User.parse_obj(result_row)
