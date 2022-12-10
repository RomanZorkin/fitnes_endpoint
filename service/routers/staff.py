from fastapi import APIRouter

router = APIRouter()


@router.get('/team/get_employees/')
def read_team():
    return {"username": "fakecurrentuser"}
