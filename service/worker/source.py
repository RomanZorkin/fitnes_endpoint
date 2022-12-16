from typing import Any

import httpx

from service import schemas
from service.repos.rule import EndpointRepo

endpoint_repo = EndpointRepo()


def get_team() -> list[dict[str, Any]]:

    rules = endpoint_repo.get_by_uid(uid=1)
    endpoint_config = schemas.Endpoint.from_orm(rules)
    endpoint_config.data.clubid = endpoint_config.clubid

    response = httpx.post(
        endpoint_config.url,
        auth=(endpoint_config.user, endpoint_config.password),
        json=endpoint_config.data.dict(),
    )
    team = response.json()[endpoint_config.contentname]
    return [schemas.Staff(**person).dict(by_alias=False) for person in team]
