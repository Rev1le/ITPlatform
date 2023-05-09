import sqlalchemy
from app.db import entities, tokens_table, users_table, vacancies_table, vacancy_skills_table, skills_table, database


async def get_mentor_by_uuid_async(mentor_uuid: str) -> entities.Mentor:

    with open("./app/db/queries/sql_queries/get_mentor_by_uuid.sql") as f:
        query = f.read()
    print(query)

    result_row = await database.fetch_one(query=query, values={"uuid": mentor_uuid})

    return parse_row_to_mentor(result_row)


def parse_row_to_mentor(row) -> entities.Mentor:
    dict_row = dict(row)
    try:
        dict_row["skills"] = dict_row["skills"].split(', ')
    except AttributeError:
        dict_row["skills"] = []

    user = entities.User.parse_obj(dict_row)
    dict_row['user'] = user
    return entities.Mentor.parse_obj(dict_row)
