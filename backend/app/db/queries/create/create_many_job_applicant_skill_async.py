import sqlalchemy
from app.db import entities, job_applicant_skills_table, database, Skill


async def create_many_job_applicant_skill(job_appicant_uuid: str, skills: list[Skill]):

    values = list(map(lambda skill: (job_appicant_uuid, skill.uuid), skills))
    print(values)

    query = job_applicant_skills_table.insert(values)
    print(query)

    await database.execute(query)
