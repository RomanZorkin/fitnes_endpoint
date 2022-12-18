from fastapi import FastAPI

from service import config
from service.routers import staff

app_config = config.load_from_env()


def create_app():
    app_fastapi = FastAPI()
    app_fastapi.include_router(staff.router)

    return app_fastapi
