from typing import Annotated, TypeAlias

from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader

from app import db
from app.db.queries.get.get_user_by_auth_token_async import get_user_by_auth_token
from app.logger import Logger


token_header = APIKeyHeader(name="Token")
logger = Logger()


async def get_logger() -> Logger:
    return logger


GetLogger: TypeAlias = Annotated[Logger, Depends(get_logger)]


async def check_auth_user_token(
    token: Annotated[str, Depends(token_header)],
    loger: GetLogger
) -> db.User:

    user = await get_user_by_auth_token(token)

    loger.log(f"\nResult user token => {user}\n")

    if user is None:
        raise HTTPException(
            status_code=400,
            detail={"message": "Invalid token in headers"}
        )

    return user


AuthUser: TypeAlias = Annotated[db.User, Depends(check_auth_user_token)]