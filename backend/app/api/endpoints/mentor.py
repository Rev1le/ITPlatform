from fastapi import APIRouter

from app.core.database import edgedb_client
from app.queries.get_mentors_async_edgeql import GetMentorsResult, get_mentors


router = APIRouter()

@router.get("/all")
async def get_all_mentors() -> list[GetMentorsResult]:
    return await get_mentors(edgedb_client)
