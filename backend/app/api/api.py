from fastapi import APIRouter

from app.api.endpoints import (
    auth,
    mentor,
    registration,
    task_blocks,
    update_user_data,
    vacancy,
)

api_router = APIRouter()
api_router.include_router(registration.router, prefix="/registration")
api_router.include_router(auth.router, prefix="/auth")
api_router.include_router(vacancy.router, prefix="/vacancy")
api_router.include_router(mentor.router, prefix="/mentor")
api_router.include_router(update_user_data.router, prefix="/update")
api_router.include_router(task_blocks.router, prefix="/task_block")
