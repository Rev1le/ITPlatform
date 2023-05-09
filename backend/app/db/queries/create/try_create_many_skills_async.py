import uuid
from app.db import entities, skills_table, database


async def try_create_many_skills(skills_name: list[str]) -> (list[entities.Skill], list[entities.Skill]):

    created_skills = await get_created_skills(skills_name)
    created_skills_names = list(map(lambda skill: skill.name, created_skills))

    need_create_skills_name = list(filter(lambda skill_name: skill_name not in created_skills_names, skills_name))

    if len(need_create_skills_name) == 0:
        return created_skills, []

    need_create_skills = list(map(lambda skill_name: entities.Skill(uuid=str(uuid.uuid4()), name=skill_name), need_create_skills_name))

    query = skills_table \
        .insert() \
        .values(list(map(lambda skill: skill.dict(), need_create_skills)))
    print(query)

    await database.execute(query)

    return created_skills, need_create_skills


async def get_created_skills(skills_name: list[str]) -> list[entities.Skill]:
    query = skills_table.select().where(skills_table.c.name not in skills_name)

    print(query)

    result_rows = await database.fetch_all(query)

    #return list(map(lambda row: dict(row)["name"], result_rows))
    return list(map(lambda row: entities.Skill.parse_obj(dict(row)), result_rows))
