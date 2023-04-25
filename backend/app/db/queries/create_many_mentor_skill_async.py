import sqlalchemy
from app.db import entities, mentor_skills_table, database


async def create_many_mentor_skill(mentor_uuid: str, skills: list[entities.Skill]):

    values = list(map(
        lambda skill: (mentor_uuid, skill.uuid),
        skills
    ))
    print(values)

    query = mentor_skills_table.insert(values)
    print(query)

    await database.execute(query)
