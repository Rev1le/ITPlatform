from app.db import entities, task_blocks_table, database


async def create_task_block(task_block: entities.TaskBlock):

    task_block_dict = task_block.dict()

    query = task_blocks_table\
        .insert()\
        .values(task_block_dict)

    await database.execute(query)
