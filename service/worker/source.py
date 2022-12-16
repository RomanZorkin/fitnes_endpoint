from typing import Any

import httpx

from service import config, schemas

endpoint_config = config.load_from_env().endpoint


def get_team() -> list[dict[str, Any]]:
    response = httpx.post(
        endpoint_config.url,
        auth=(endpoint_config.user, endpoint_config.password),
        json=endpoint_config.data,
    )
    team = response.json()[endpoint_config.contentname]
    return [schemas.Staff(**person).dict(by_alias=False) for person in team]
