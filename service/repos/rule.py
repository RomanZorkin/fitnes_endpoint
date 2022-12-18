from fastapi import HTTPException
from sqlalchemy.future import select

from service.db import async_session
from service.models import Endpoint


class EndpointRepo:

    async def get_endpoint(self, uid: int):
        async with async_session() as session:
            result = await session.execute(
                select(Endpoint).where(Endpoint.id == uid),
            )
            if not result:
                raise HTTPException(status_code=404, detail='Item not found')
            answer = result.first()[0]
        return answer
