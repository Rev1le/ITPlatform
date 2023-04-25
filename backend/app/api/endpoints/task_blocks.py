import asyncio
import sqlite3
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from starlette.background import BackgroundTasks




class Question(BaseModel):
    id: UUID
    answer: str


class Code(BaseModel):
    id: UUID
    lang: str
    answer: str


class Answers(BaseModel):
    questions: list[Question]
    codes: list[Code]


router = APIRouter()


# @router.get("/all")
# async def all_tasks_blocks(job_applicant: AuthJobApplicant) -> list[GetTaskBlocksResult]:
#     return await get_task_blocks(edgedb_client, user_id=job_applicant.uuid)
#
#
# @router.post("/")
# async def create_task_block(task_block: TaskBlock, employer: AuthEmployer):
#     try:
#         await db.create_task_block(task_block)
#     except sqlite3.IntegrityError as e:
#         print("Create task_block with error =>", e)
#         raise HTTPException(status_code=404, detail={"message": "Invalid create task block"})
#
#
# @router.get("/{id}")
# async def task_block_info(
#     id: UUID,
#     worker: Annotated[GetWorkerByTokenResult, Depends(check_auth_job_applicant_token)],
# ) -> GetTaskBlockResult:
#     result = await get_task_block(edgedb_client, user_id=worker.id, task_block_id=id)
#     if result is None:
#         raise HTTPException(status_code=404, detail={"message": "Unknown task block"})
#     return result
#
#
# @router.get("/{id}/challenges")
# async def task_block_challenges(
#     id: UUID,
#     worker: Annotated[GetWorkerByTokenResult, Depends(check_auth_job_applicant_token)],
# ) -> GetTaskBlockChallengesResult:
#     result = await get_task_block_challenges(edgedb_client, task_block_id=id)
#     if result is None:
#         raise HTTPException(status_code=404, detail={"message": "Unknown task block"})
#     return result
#
#
# async def check_answers(
#     task_block_id: UUID, answers: Answers, worker: GetWorkerByTokenResult
# ):
#     right_answers = await get_answers(edgedb_client, task_block_id=task_block_id)
#     question_answers = {i.id: i.answer for i in answers.questions}
#     code_answers = {i.id: i.answer for i in answers.codes}
#
#     right_answers_count = 0
#     right_codes_count = 0
#
#     for i in right_answers.questions:
#         worker_answer = question_answers[i.id]
#         if i.right_answer == worker_answer:
#             right_answers_count += 1
#
#     for i in right_answers.codes:
#         successful_test_count = 0
#         worker_answer = code_answers[i.id]
#         cmd = f'py -c "{worker_answer}"'
#         for test in i.tests:
#             proc = await asyncio.create_subprocess_shell(
#                 cmd, stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE
#             )
#             stdout, _ = await proc.communicate(input=test.input.encode())
#             if stdout.decode().strip() == test.output:
#                 successful_test_count += 1
#         if successful_test_count == len(i.tests):
#             right_codes_count += 1
#
#     if right_answers_count == len(right_answers.questions) and right_codes_count == len(
#         right_answers.codes
#     ):
#         await complete_task_block(
#             edgedb_client, task_block_id=task_block_id, user_id=worker.id
#         )
#     else:
#         await fail_task_block(
#             edgedb_client, task_block_id=task_block_id, user_id=worker.id
#         )
#
#
# @router.post("/{id}")
# async def send_answers(
#     id: UUID,
#     answers: Answers,
#     worker: Annotated[GetWorkerByTokenResult, Depends(check_auth_job_applicant_token)],
#     background_tasks: BackgroundTasks,
# ):
#     background_tasks.add_task(check_answers, id, answers, worker)
#     return {"status": "ok"}
