from fastapi import APIRouter
from pydantic import BaseModel

class Registartion(BaseModel):
    email: str
    password: str

router = APIRouter()

@router.post("/")
async def registration_account(registration_data: Registration):
    
    try:
        created_user = await create_user_qry.create_user(client, name=user.name)
    
    except edgedb.errors.ConstraintViolationError:
        return JSONResponse(
            status_code=404, 
            content={"message": f"User with email {registration_data.email} already exists"}
            )

    return created_user

