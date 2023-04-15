from typing import Annotated, TypeVar

from fastapi import Depends, HTTPException
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
    employer = await get_employer_by_token(token)

    if employer == None:
        raise HTTPException(status_code=400, detail={"message": "Invalid token in headers"})

    return employer


async def check_auth_worker_token(
    token: Annotated[str, Depends(token_header)]
) -> GetWorkerByTokenResult:

    worker = await get_worker_by_token(token)

    if employer == None:
        raise HTTPException(status_code=400, detail={"message": "Invalid token in headers"})

    return worker
