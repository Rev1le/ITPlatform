from fastapi import APIRouter
from pydantic import BaseModel


class Registration(BaseModel):
    email: str
    password: str


router = APIRouter()


@router.post("/")
async def registration_account(registration_data: Registration):
    pass
