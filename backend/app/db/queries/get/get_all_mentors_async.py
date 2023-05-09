import sqlalchemy
from app.db import entities, mentors_table, database


async def get_all_mentors() -> list[entities.Mentor]:

    with open("./app/db/queries/sql_queries/get_all_mentors.sql") as f:
        query = f.read()
    print(query)

    result_rows = await database.fetch_all(query)

    return list(map(lambda row: parse_row_to_mentor(row), result_rows))


def parse_row_to_mentor(row) -> entities.Mentor:
    dict_row = dict(row)
    try:
        dict_row["skills"] = dict_row["skills"].split(', ')
    except AttributeError:
        dict_row["skills"] = []

    user = entities.User.parse_obj(dict_row)
    dict_row['user'] = user

    return entities.Mentor.parse_obj(dict_row)