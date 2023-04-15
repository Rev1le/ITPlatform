from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings

from app.api.api import api_router

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url="api/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")
