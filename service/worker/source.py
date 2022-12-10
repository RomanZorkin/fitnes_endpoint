import httpx

data = {
    'Request_id': 'e1477272-88d1-4acc-8e03-7008cdedc81e',
    'ClubId': '59115d1e-9052-11eb-810c-6eae8b56243b',
    'Method': 'GetSpecialistList',
    'Parameters': {'ServiceId': ''},
}

response = httpx.post(
    'http://176.192.70.122:90/fitnes_t_nfc_mobile/hs/nfc_mobile/v1',
    auth=('FitnessKit', 'vY0xodyg'),
    json=data,
)

body = response.json()['Parameters']

from typing import Optional
from pydantic import BaseModel, constr, Field


class Staf(BaseModel):

    uid: str = Field(alias='ID')
    name: str = Field(alias='Name')
    surname: str = Field(alias='Surname')
    phone: Optional[int] = Field(alias='Phone')
    photo: Optional[str] = Field(alias='Photo')


staf_list = [Staf(**person) for person in body]
print(staf_list[0].uid)