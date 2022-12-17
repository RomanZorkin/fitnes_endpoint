from fastapi import APIRouter

from service import schemas
from service.worker import source

router = APIRouter()


@router.get('/team/get_employees/')
async def read_team():
    team = await source.get_team()
    return schemas.Answer(**{
        'team': [schemas.Staff(**person).dict(by_alias=False) for person in team],
    })
