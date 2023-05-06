import sqlalchemy
from app.db import entities, vacancies_table, database, vacancy_skills_table, skills_table


async def create_vacancy(vacancy: entities.Vacancy):

    params = vacancy.dict()
    skills_names = params.pop("skills")

    query_create_vacancy = sqlalchemy\
        .insert(vacancies_table)\
        .values(**params)

    await database.execute(query_create_vacancy)

    sel = sqlalchemy \
        .select(
            vacancies_table.c.uuid,
            skills_table.c.uuid
        )\
        .where(skills_table.c.name.in_(skills_names)) \
        .where(vacancies_table.c.uuid == vacancy.uuid)

    query_create_vacancy_skills = sqlalchemy \
        .insert(vacancy_skills_table) \
        .from_select(
            names=['vacancy_uuid', 'skill_uuid'],
            select=sel,
            include_defaults=True
        )

    await database.execute(query_create_vacancy_skills)
