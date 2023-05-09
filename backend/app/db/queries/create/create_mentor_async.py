import sqlalchemy

from app.db import entities, mentors_table, skills_table, mentor_skills_table, database


async def create_mentor(mentor: entities.Mentor):

    params = mentor.dict()
    skills_names = params.pop("skills")

    query_create_vacancy = sqlalchemy \
        .insert(mentors_table) \
        .values(**params)

    await database.execute(query_create_vacancy)

    sel = sqlalchemy \
        .select(
            mentors_table.c.uuid,
            skills_table.c.uuid
        )\
        .where(skills_table.c.name.in_(skills_names)) \
        .where(mentors_table.c.uuid == mentor.uuid)

    query_create_vacancy_skills = sqlalchemy \
        .insert(mentor_skills_table) \
        .from_select(
            names=['mentor_uuid', 'skill_uuid'],
            select=sel,
            include_defaults=True
        )

    await database.execute(query_create_vacancy_skills)
