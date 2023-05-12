import json
import pydantic
import sqlalchemy
from app.db import entities, mentors_table, task_blocks_table, database, QuestionResponse


async def get_all_task_block() -> list[entities.TaskBlock]:

    query = sqlalchemy.select(task_blocks_table)
    result_rows = await database.fetch_all(query)

    return pydantic.parse_obj_as(list[entities.TaskBlock], result_rows)
