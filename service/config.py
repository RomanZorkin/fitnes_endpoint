import os

from pydantic import BaseModel


class AppConfig(BaseModel):
    endpoint: str
    app_port: str
    app_host: str
    user: str
    password: str


def load_from_env() -> AppConfig:
    return AppConfig(
        endpoint=os.environ['ENDPOINT'],
        app_port=os.environ['APP_PORT'],
        app_host=os.environ['APP_HOST'],
        user=os.environ['USER'],
        password=os.environ['PASSWORD']
    )
