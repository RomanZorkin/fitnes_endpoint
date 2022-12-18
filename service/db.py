from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from service import config

app_config = config.load_from_env().db

engine = create_async_engine(app_config.db_url)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
