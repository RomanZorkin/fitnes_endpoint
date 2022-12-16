from fastapi import FastAPI

from service import config
from service.routers import staff
from service.worker import home

app_config = config.load_from_env()


def create_app():
    app_fastapi = FastAPI()
    app_fastapi.include_router(staff.router)

    @app_fastapi.get('/')
    def root():
        return {'message': home.get_dir()}

    return app_fastapi
