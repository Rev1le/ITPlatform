import pprint

import sqlalchemy

from app.db.entities import task_blocks_table, questions_table, question_options_table
from app.db import database


async def get_task_block(task_block_uuid: str):
    query = sqlalchemy\
        .select(task_blocks_table)\
        .where(task_blocks_table.c.uuid == task_block_uuid)
    result_row_tb = await database.fetch_one(query)

    query = sqlalchemy \
        .select(questions_table) \
        .where(questions_table.c.task_block_uuid == task_block_uuid)
    result_rows_qs = await database.fetch_all(query)

    question_list = list(map(lambda row: dict(row), result_rows_qs))
    question_uuid_list = list(map(lambda row: dict(row)['uuid'], result_rows_qs))

    query = sqlalchemy \
        .select(question_options_table) \
        .where(question_options_table.c.question_uuid.in_(question_uuid_list))
    result_rows_qv = await database.fetch_all(query)

    print(result_rows_qv)

    task_block = {**result_row_tb, 'questions': []}

    for question in question_list:
        question_var = list(filter(lambda qv: dict(qv)['question_uuid'] == question['uuid'], result_rows_qv))
        task_block['questions'].append({'q': question, 'question_variants': question_var})

    print()
    pprint.pprint(task_block)




def parse_task_block(rows):

    obj_dict = dict()
    #obj_dict['questions'] = []

    for row in rows:
        dict_row = dict(row)
        pprint.pprint(dict_row)

        for key, value in dict_row.items():
            if key in obj_dict:
                try:
                    obj_dict[key].append(value)
                except AttributeError:
                    obj_dict[key] = value
            else:
                obj_dict[key] = [value]

    print('\n\n')
    pprint.pprint(obj_dict)

