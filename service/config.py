import os

from pydantic import BaseModel


class DataBase(BaseModel):
    db_url: str


class Host(BaseModel):
    app_port: int
    app_host: str


class AppConfig(BaseModel):
    host: Host
    db: DataBase


def load_from_env() -> AppConfig:
    return AppConfig(
        host=Host(
            app_port=os.environ['APP_PORT'],
            app_host=os.environ['APP_HOST'],
        ),
        db=DataBase(
            db_url=os.environ['DATABASE_URL'],
        ),
    )
