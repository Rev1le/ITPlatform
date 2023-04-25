import sqlalchemy
from app.db import entities, job_applicant_table, database


async def create_job_applicant(job_applicant: entities.JobApplicant):
    query = sqlalchemy\
        .insert(job_applicant_table)\
        .values(job_applicant.dict())
    await database.execute(query)