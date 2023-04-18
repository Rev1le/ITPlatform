# AUTOGENERATED FROM 'app/queries/get_task_block_challenges.edgeql' WITH:
#     $ python.exe -m edgedb.codegen


from __future__ import annotations
import dataclasses
import edgedb
import uuid


class NoPydanticValidation:
    @classmethod
    def __get_validators__(cls):
        from pydantic.dataclasses import dataclass as pydantic_dataclass
        pydantic_dataclass(cls)
        cls.__pydantic_model__.__get_validators__ = lambda: []
        return []


@dataclasses.dataclass
class GetTaskBlockChallengesResult(NoPydanticValidation):
    id: uuid.UUID
    questions: list[GetTaskBlockChallengesResultQuestionsItem]
    codes: list[GetTaskBlockChallengesResultCodesItem]


@dataclasses.dataclass
class GetTaskBlockChallengesResultCodesItem(NoPydanticValidation):
    id: uuid.UUID
    question: str


@dataclasses.dataclass
class GetTaskBlockChallengesResultQuestionsItem(NoPydanticValidation):
    id: uuid.UUID
    question: str
    answers: list[str]


async def get_task_block_challenges(
    executor: edgedb.AsyncIOExecutor,
    *,
    task_block_id: uuid.UUID,
) -> GetTaskBlockChallengesResult | None:
    return await executor.query_single(
        """\
        select TaskBlock {
            questions := .questions {
                id,
                question,
                answers
            },
            codes := .codes {
                id,
                question
            }
        }
        filter .id = <uuid>$task_block_id\
        """,
        task_block_id=task_block_id,
    )
