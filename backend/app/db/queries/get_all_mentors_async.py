import sqlalchemy
from app.db import entities, mentors_table, database


async def get_all_mentors() -> list[entities.Mentor]:
    query = sqlalchemy.select(mentors_table)
    print(query)

    result_rows = await database.fetch_all(query)

    return list(map(
        lambda row: entities.Mentor.parse_obj(dict(row)),
        result_rows
    ))