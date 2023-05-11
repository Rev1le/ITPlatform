from fastapi import APIRouter

from app.api.endpoints import (
    mentor,
    task_block,
    update_user_data,
    vacancy,
    user
)

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user")
api_router.include_router(user.router, prefix="/job_applicant")
api_router.include_router(vacancy.router, prefix="/vacancy")
api_router.include_router(mentor.router, prefix="/mentor")
api_router.include_router(update_user_data.router, prefix="/update")
api_router.include_router(task_block.router, prefix="/task_block")
