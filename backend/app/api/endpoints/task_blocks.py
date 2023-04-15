from fastapi import APIRouter

from app.core.database import edgedb_client


router = APIRouter()


@router.get("/")
def get_all_tasks_blocks():
    pass
