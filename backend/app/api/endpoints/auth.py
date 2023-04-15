from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import hashlib
import secrets
from app.queries.get_worker_by_hash_async_edgeql import get_worker_by_hash
from app.queries.get_employer_by_hash_async_edgeql import get_employer_by_hash
from app.queries.create_worker_token_async_edgeql import create_worker_token
from app.queries.create_employer_token_async_edgeql import create_employer_token
from app.core.database import edgedb_client

class Login(BaseModel):
    email: str
    password: str

class LoginAccess():
    token: str

router = APIRouter()

@router.post("/employer")
async def auth_employer(login: Login):
    password_hash = hashlib.sha256(login.password.hexdigest())
    
    employer = await get_employer_by_hash(
        edgedb_client, 
        hash = password_hash, 
        email = login.email
        )
    
    if employer == None:
        return JSONResponse(
            status_code=404, 
            content={"message": "Ivalid login data"}
            )

    auth_token = secrets.token_urlsafe(32)
    
    await create_employer_token(edgedb_client, auth_token, employer.id)

    return LoginAccess(token = auth_token)

@router.post("/worker")
async def auth_worker(login: Login) -> LoginAccess | JSONResponse:
    
    password_hash = hashlib.sha256(login.password.hexdigest())
    
    worker = await get_worker_by_hash(
        edgedb_client, 
        hash = password_hash, 
        email = login.email
        )
    
    if worker == None:
        return JSONResponse(
            status_code=404, 
            content={"message": "Ivalid login data"}
            )

    auth_token = secrets.token_urlsafe(32)
    
    await create_worker_token(edgedb_client, auth_token, worker.id)

    return LoginAccess(token = auth_token)
