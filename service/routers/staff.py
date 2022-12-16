from fastapi import APIRouter

from service import schemas
from service.repos.rule import EndpointRepo
from service.worker import source

router = APIRouter()

endpoint_repo = EndpointRepo()


@router.get('/team/get_employees/')
def read_team():
    team = source.get_team()
    return {'team': team}


@router.get('/db/')
def read_bd():
    rules = endpoint_repo.get_by_uid(uid=1)
    ghj = schemas.Endpoint.from_orm(rules)
    print(ghj)
    return {'rule': rules}
