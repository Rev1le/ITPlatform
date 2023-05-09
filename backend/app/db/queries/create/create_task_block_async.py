from app.db import entities, task_blocks_table, questions_table, question_options_table, database


async def create_task_block(task_block: entities.TaskBlock):

    task_block_dict = task_block.dict()

    questions = task_block_dict.pop('questions')
    print('Questions:', questions)

    query = task_blocks_table\
        .insert()\
        .values(task_block_dict)

    await database.execute(query)

    for question in questions:
        await execute_question(question, task_block_dict['uuid'])


async def execute_question(question, task_block_uuid: str):
    uuid = question['uuid']

    variants = question.pop('variants')
    variants = list(map(lambda variant: dict({'question_uuid': uuid, **variant}), variants))

    print(variants)

    query = question_options_table \
        .insert() \
        .values(variants)

    await database.execute(query)

    #print("Остаток от Question: ", question)

    question.update({'task_block_uuid': task_block_uuid})

    query = questions_table \
        .insert() \
        .values(question)

    await database.execute(query)

