import sqlalchemy
from app.db import entities, database


async def get_all_vacancies() -> list[entities.Vacancy]:

    with open("./app/db/queries/sql_queries/get_all_vacancies.sql") as f:
        query = f.read()
    print(query)

    result_rows = await database.fetch_all(query)

    return list(map(lambda row: parse_row_to_vacancy(row), result_rows))


def parse_row_to_vacancy(row):
    dict_row = dict(row)
    try:
        dict_row["skills"] = dict_row["skills"].split(', ')
    except AttributeError:
        dict_row["skills"] = []

    return entities.Vacancy.parse_obj(dict_row)