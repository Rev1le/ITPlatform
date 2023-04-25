import secrets
from app.db import entities, tokens_table, database


async def create_auth_token(user_uuid: str) -> entities.AuthToken:
    auth_token = entities.AuthToken(
        token=secrets.token_urlsafe(32),
        owner_uuid=user_uuid
    )

    query = tokens_table \
        .insert() \
        .values(auth_token.dict())

    await database.execute(query)

    return auth_token