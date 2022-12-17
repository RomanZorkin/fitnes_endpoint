from fastapi import APIRouter

from service.worker import source

router = APIRouter()


@router.get('/team/get_employees/')
async def read_team():
    team = await source.get_team()
    return {'team': team}
