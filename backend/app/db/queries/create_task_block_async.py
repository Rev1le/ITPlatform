from app.db import entities, task_blocks_table, database


async def create_task_block(task_block: entities.TaskBlock):
    query = task_blocks_table\
        .insert()\
        .values(task_block.dict())

    await database.execute(query)