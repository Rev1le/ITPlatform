from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_all_vacancies():
    # select * from vacancy
    ...
