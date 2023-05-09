import sqlalchemy
from app.db import entities, tokens_table, users_table, vacancies_table, vacancy_skills_table, skills_table, database


async def get_vacancy_by_uuid_async(vacancy_uuid: str) -> entities.Vacancy:

    with open("./app/db/queries/sql_queries/get_vacancy_by_uuid.sql") as f:
        query = f.read()
    print(query)

    result_row = await database.fetch_one(query=query, values={"uuid": vacancy_uuid})

    return parse_row_to_vacancy(result_row)


def parse_row_to_vacancy(row) -> entities.Vacancy:
    dict_row = dict(row)
    try:
        dict_row["skills"] = dict_row["skills"].split(', ')
    except AttributeError:
        dict_row["skills"] = []

    return entities.Vacancy.parse_obj(dict_row)
