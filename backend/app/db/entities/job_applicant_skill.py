from sqlalchemy import Table, Column, Integer, String, Text, Date, ARRAY, ForeignKey
from . import metadata

job_applicant_skills_table = Table(
    'job_applicant_skill',
    metadata,
    Column('job_applicant_uuid', ForeignKey('job_applicant.uuid'), primary_key=True),
    Column('skill_uuid', ForeignKey('skill.uuid'), primary_key=True)
)