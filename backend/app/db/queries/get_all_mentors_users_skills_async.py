import datetime

import sqlalchemy
from pydantic import BaseModel
from app.db import entities, mentors_table, database, users_table, mentor_skills_table, skills_table


class MentorUser(BaseModel):
    uuid: str
    name: str
    salary: float
    skills: list[str]
    resume: str | None
    birthday: datetime.date
    bio: str | None
    photo: str | None


async def get_all_mentors_users_skills():

    with open("./app/db/queries/get_all_mentors_users_skills.sql") as f:
        query = f.read()
        result_rows = await database.fetch_all(query)

        return list(map(lambda row: get_mentor_user(row), result_rows))


def get_mentor_user(row):
    dict_row = dict(row)
    dict_row["skills"] = dict_row["skills"].split(', ')

    return MentorUser.parse_obj(dict_row)


# async def create_mentor_user(row) -> str:
#     dict_row = dict(row)
#     mentor_uuid = dict_row["uuid"]
#
#     query_skills = sqlalchemy \
#         .select(skills_table.c.name) \
#         .join(mentor_skills_table, mentor_skills_table.c.mentor_uuid == skills_table.c.uuid, isouter=True) \
#         .where(mentor_skills_table.c.mentor_uuid == mentor_uuid)
#     print("Query skills", query_skills)
#
#     skills_rows = await database.execute(query_skills)
#     print(skills_rows)
#     print(dict(skills_rows))
#     return "Hi"
    # return MentorUser.parse_obj(dict_row)

# SELECT skill.name FROM skill
# LEFT JOIN mentor_skill ON mentor_skill.skill_uuid == skill.uuid
# WHERE mentor_skill.mentor_uuid == "d6e6c181-55ac-480d-8f6c-5677dd58d12a"
