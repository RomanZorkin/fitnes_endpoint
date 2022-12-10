import httpx

from service import config, schemas

app_config = config.load_from_env()

data = {
    'Request_id': 'e1477272-88d1-4acc-8e03-7008cdedc81e',
    'ClubId': '59115d1e-9052-11eb-810c-6eae8b56243b',
    'Method': 'GetSpecialistList',
    'Parameters': {'ServiceId': ''},
}


def get_team() -> list[schemas.Staf]:

    response = httpx.post(
        app_config.endpoint,
        auth=(app_config.user, app_config.password),
        json=data,
    )

    body = response.json()['Parameters']
    return [schemas.Staf(**person) for person in body]
