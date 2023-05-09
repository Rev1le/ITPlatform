import sqlalchemy
from app.db import entities, employers_table, database

async def create_employer(employer: entities.Employer):
    query = sqlalchemy\
        .insert(employers_table)\
        .values(employer.dict())

    await database.execute(query)
    