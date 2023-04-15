from typing import Annotated, TypeVar

from fastapi import Depends
from fastapi.security import APIKeyHeader

from app.queries.get_employer_by_token_async_edgeql import (
    GetEmployerByTokenResult,
    get_employer_by_token,
)
from app.queries.get_worker_by_token_async_edgeql import (
    GetWorkerByTokenResult,
    get_worker_by_token,
)

token_header = APIKeyHeader(name="token")
AuthEmplayer = TypeVar('Annotated[GetEmployerByTokenResult, Depends(check_auth_employer_token)]')


async def check_auth_employer_token(
    token: Annotated[str, Depends(token_header)]
) -> GetEmployerByTokenResult:
    return await get_employer_by_token(token)


async def check_auth_worker_token(
    token: Annotated[str, Depends(token_header)]
) -> GetWorkerByTokenResult:
    return await get_worker_by_token(token)
