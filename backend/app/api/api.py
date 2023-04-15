from fastapi import APIRouter

from app.api.endpoints import auth, vacancy, registration

api_router = APIRouter()
api_router.include_router(registration.router, prefix="/registration")
api_router.include_router(auth.router, prefix="/auth")
api_router.include_router(vacancy.router, prefix="/vacancy")
