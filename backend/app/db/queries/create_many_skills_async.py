import uuid

import sqlalchemy
from app.db import entities, skills_table, database


async def create_many_skills(skills: list[entities.Skill]):

    values = list(map(lambda skill: skill.dict(), skills))

    query = sqlalchemy.insert(skills_table)
    #print(query)
    print(query)
    await database.execute_many(query, values)