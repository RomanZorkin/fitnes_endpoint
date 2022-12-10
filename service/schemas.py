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
