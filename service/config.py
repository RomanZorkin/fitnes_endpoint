import os

from pydantic import BaseModel

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class DataBase(BaseModel):
    db_url: str


class Endpoint(BaseModel):
    url: str
    user: str
    password: str
    contentname = 'Parameters'
    data = {
        'Request_id': 'e1477272-88d1-4acc-8e03-7008cdedc81e',
        'ClubId': '59115d1e-9052-11eb-810c-6eae8b56243b',
        'Method': 'GetSpecialistList',
        'Parameters': {'ServiceId': ''},
    }


class Host(BaseModel):
    app_port: int
    app_host: str


class AppConfig(BaseModel):
    endpoint: Endpoint
    host: Host
    db: DataBase


def load_from_env() -> AppConfig:
    return AppConfig(
        endpoint=Endpoint(
            url=os.environ['ENDPOINT'],
            user=os.environ['USER'],
            password=os.environ['PASSWORD'],
        ),
        host=Host(
            app_port=os.environ['APP_PORT'],
            app_host=os.environ['APP_HOST'],
        ),
        db=DataBase(
            db_url=os.environ['DATABASE_URL'],
        ),
    )
