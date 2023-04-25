import sqlalchemy
from app.db import entities, users_table, database


async def create_user(user: entities.User):
    query = sqlalchemy\
        .insert(users_table)\
        .values(user.dict())
    await database.execute(query)