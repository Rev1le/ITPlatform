import sqlalchemy
from app.db import entities, skills_table, database


async def create_many_skills(skills: list[entities.Skill]):
    query = sqlalchemy.insert(skills_table)

    values = list(map(lambda skill: skill.dict(), skills))

    #print(query, values)
    await database.execute_many(query, values)