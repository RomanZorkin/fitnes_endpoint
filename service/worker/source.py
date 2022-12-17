from typing import Any

import httpx
from fastapi import HTTPException

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
        response = httpx.post(
            endpoint_config.url,
            auth=(endpoint_config.user, endpoint_config.password),
            json=endpoint_config.data.dict(),
        )
        code = response.status_code
        if code != 200:
            text = response.text
            raise HTTPException(status_code=500, detail=f'Server error: status {code} {text}')
        return response

    except httpx.HTTPError as exc:
        raise HTTPException(status_code=500, detail=f'Server error {exc}')


def get_team() -> list[dict[str, Any]]:
    endpoint_config = get_settings(uid=2)
    response = get_response(endpoint_config)
    team = response.json().get(endpoint_config.contentname, None)

    if not team:
        raise HTTPException(
            status_code=400,
            detail='Error processing the received data. Perhaps the structure of the response has\
changed',
        )

    return [schemas.Staff(**person).dict(by_alias=False) for person in team]
