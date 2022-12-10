from typing import Optional

from pydantic import BaseModel, Field


class Staff(BaseModel):

    uid: str = Field(alias='ID')
    name: str = Field(alias='Name')
    surname: str = Field(alias='Surname')
    phone: Optional[int] = Field(alias='Phone')
    photo: Optional[str] = Field(alias='Photo')
