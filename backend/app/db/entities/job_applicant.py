from typing import List
from pydantic import BaseModel
import datetime
from sqlalchemy import Table, Column, Integer, String, Text, Date, ARRAY, ForeignKey
from . import metadata


class JobApplicant(BaseModel):
    uuid: str
    resume: str | None


job_applicant_table = Table(
    'job_applicant',
    metadata,
    Column('uuid', String(128), primary_key=True),
    Column('resume', Text),
)