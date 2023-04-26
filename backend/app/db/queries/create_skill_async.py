import uuid
from app.db import entities, skills_table, database


async def create_skill(skill_name: str) -> entities.Skill:
    skill = entities.Skill(
        uuid=str(uuid.uuid4()),
        name=skill_name
    )

    query = skills_table \
        .insert() \
        .values(skill.dict())

    await database.execute(query)

    return skill
