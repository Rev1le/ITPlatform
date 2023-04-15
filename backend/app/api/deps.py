from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, APIKeyHeader
from app.queries.get_employer_by_token_async_edgeql import get_employer_by_token, GetEmployerByTokenResult
from app.queries.get_worker_by_token_async_edgeql import get_worker_by_token, GetWorkerByTokenResult


token_header = APIKeyHeader(name="token")


async def check_auth_employer_token(token: Annotated[str, Depends(token_header)]) -> GetEmployerByTokenResult:
    return await get_employer_by_token(token)

async def check_auth_worker_token(token: Annotated[str, Depends(token_header)]) -> GetWorkerByTokenResult:
    return await get_worker_by_token(token)