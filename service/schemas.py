from typing import Optional

from pydantic import BaseModel, Field


class Staff(BaseModel):

    id: str = Field(alias='ID')
    name: str = Field(alias='Name')
    last_name: str = Field(alias='Surname')
    phone: Optional[int] = Field(alias='Phone')
    image_url: Optional[str] = Field(alias='Photo')

    class Config:
        allow_population_by_field_name = True


class EndpointData(BaseModel):
    request_id: str = Field('e1477272-88d1-4acc-8e03-7008cdedc81e', alias='Request_id')
    clubid: str = Field('', alias='ClubId')
    method: str = Field('GetSpecialistList', alias='Method')
    parameters: dict[str, str] = Field({'ServiceId': ''}, alias='Parameters')


class Endpoint(BaseModel):
    id: int
    url: str
    user: str = Field(alias='login')
    password: str
    contentname = 'Parameters'
    clubid: str
    data: EndpointData = EndpointData()

    class Config:
        orm_mode = True
