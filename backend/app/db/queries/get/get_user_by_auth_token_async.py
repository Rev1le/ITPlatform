import sqlalchemy
from app.db import entities, tokens_table, users_table, database


async def get_user_by_auth_token(auth_token: str) -> entities.User:
    query = sqlalchemy\
        .select(users_table)\
        .join(
            users_table,
            tokens_table.c.owner_uuid == users_table.c.uuid,
            isouter=True
        )\
        .where(tokens_table.c.token == auth_token)

    print("QUERY =======>", query)

    row_result = await database.fetch_one(query)

    print(row_result)

    return entities.User\
        .parse_obj(dict(row_result))