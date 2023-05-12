import json
import pprint

import sqlalchemy

from app.db.entities import task_blocks_table, TaskBlock, TaskBlockResponse
from app.db import database


async def get_task_block(task_block_uuid: str) -> TaskBlock:

    query = sqlalchemy\
        .select(task_blocks_table)\
        .where(task_blocks_table.c.uuid == task_block_uuid)

    result_row = await database.fetch_one(query)

    return TaskBlock.parse_obj(result_row)
