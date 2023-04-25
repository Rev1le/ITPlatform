import sqlalchemy
from app.db import entities, vacancies_table, database

async def create_vacancy(employer: entities.Vacancy):
    query = sqlalchemy\
        .insert(vacancies_table)\
        .values(employer.dict())

    await database.execute(query)