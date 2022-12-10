from fastapi import APIRouter

from service.worker import source

router = APIRouter()


@router.get('/team/get_employees/')
def read_team():
    team = source.get_team()
    return {'team': team}
