from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from service.db import engine

Base = declarative_base()


class Endpoint(Base):  # type: ignore
    __tablename__ = 'endpoint'
    id = Column(Integer, primary_key=True, autoincrement=True)
    clubid = Column(String)
    login = Column(String)
    password = Column(String)
    url = Column(String)

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return f'<Endpoint url="{self.url}" clubid="{self.clubid}">'


async def start_model():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
