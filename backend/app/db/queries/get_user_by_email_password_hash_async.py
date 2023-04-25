import sqlalchemy
from app.db import entities, users_table, database


async def get_user_by_email_password_hash(email: str, password_hash: str) -> entities.User:
    query = sqlalchemy\
        .select(users_table)\
        .where(users_table.c.email == email)\
        .where(users_table.c.password_hash == password_hash)

    row_result = await database.fetch_one(query)
    print(row_result)

    return entities.User.parse_obj(dict(row_result))