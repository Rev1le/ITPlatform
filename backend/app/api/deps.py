from typing import Annotated, TypeVar, TypeAlias

from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader

from app import db
from app.db.queries.get_user_by_auth_token_async import get_user_by_auth_token


token_header = APIKeyHeader(name="Token")


async def check_auth_user_token(
    token: Annotated[str, Depends(token_header)]
) -> db.User:

    user = await get_user_by_auth_token(token)
    print("Result user token =>", user)

    if user is None:
        raise HTTPException(
            status_code=400,
            detail={"message": "Invalid token in headers"}
        )

    return user

AuthUser: TypeAlias = Annotated[db.User, Depends(check_auth_user_token)]