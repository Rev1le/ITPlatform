from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.api.deps import AuthUser


router = APIRouter()


class MentorData(BaseModel):
    skills: list[str]
    salary: float
    resume: str

class Mentor(BaseModel):
    name: str
    vocation: str
    skills: list[str]
    salary: str
    description: str

mentors = [
    Mentor(
        name="Мария Иванова",
        vocation="Python & SQL",
        skills=["sql", "Soft", "python"],
        salary="Опытный ментор",
        description="Хочу помочь начинающим"
    ),
    Mentor(
        name="Иван Козюков",
        vocation="Python & SQL",
        skills=["sql", "python"],
        salary="Опытный ментор",
        description="Хочу помочь начинающим разработчикам"
    ),
    Mentor(
        name="Король и Шут",
        vocation="Python & SQL",
        skills=["Молнии","Дурак"],
        salary="Опытный ментор",
        description="Помогу в сборе молниц"
    ),

]

# @router.get("/all")
# async def get_all_mentors() -> list[GetMentorsResult]:
#     return await get_mentors(edgedb_client)

@router.get("/all")
async def get_all_mentors() -> list[Mentor]:
    #await test_db()
    #return await test_db()
    return []


@router.post("/")
async def create(employer: AuthUser,mentor_data: MentorData) -> str:

    #print(employer.mentor[0])

    # try:
    #     await create_mentor(
    #         edgedb_client,
    #         user_id=employer.id,
    #         skills=mentor_data.skills,
    #         salary=mentor_data.salary,
    #         resume=mentor_data.resume
    #     )
    #
    # except:
    #     raise HTTPException(status_code=404, detail={"message": "Invalid mentor data"})

    return "ok"
