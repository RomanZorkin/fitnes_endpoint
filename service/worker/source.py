from typing import Any

import httpx

from service import schemas
from service.repos.rule import EndpointRepo

endpoint_repo = EndpointRepo()


def get_settings(uid: int) -> schemas.Endpoint:

    rules = endpoint_repo.get_by_uid(uid=uid)
    endpoint_config = schemas.Endpoint.from_orm(rules)

    endpoint_config.data.clubid = endpoint_config.clubid
    
    return endpoint_config


def get_response(endpoint_config: schemas.Endpoint):
    try:
        return httpx.post(
            endpoint_config.url,
            auth=(endpoint_config.user, endpoint_config.password),
            json=endpoint_config.data.dict(),
        )
    except httpx.RequestError as exc:
        return exc.request.content


def get_team() -> list[dict[str, Any]]:
    endpoint_config = get_settings(uid=2)        
    response = get_response(endpoint_config)

    team = response.json()[endpoint_config.contentname]

    return [schemas.Staff(**person).dict(by_alias=False) for person in team]
