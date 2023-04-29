from fastapi import APIRouter

router = APIRouter()

@router.get("/all")
async def get_all_task_blocks() -> list[TaskBlock]:
    pass