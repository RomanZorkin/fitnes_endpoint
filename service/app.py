from fastapi import FastAPI
import uvicorn

from service import config
from service.routers import staff
#from service.worker import source

app_config = config.load_from_env()


def create_app():
    app_fastapi = FastAPI()
    app_fastapi.include_router(staff.router)
    #team = source.get_team()

    @app_fastapi.get('/')
    def root():
        return {'message': 'Hello Bigger Applications!'}
    return app_fastapi
    #print('hello', '\n', team)
