import asyncio

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api import api_router

asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

print("Start app ...")

app = FastAPI(title="Title", openapi_url="/api/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")