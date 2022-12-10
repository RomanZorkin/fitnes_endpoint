import os

from fastapi_admin.app import app as admin_app
from fastapi import FastAPI
from fastapi_admin.resources import Link
from starlette.staticfiles import StaticFiles

from service import config
from service.routers import staff

app_config = config.load_from_env()

login_provider = UsernamePasswordProvider(
    admin_model=Admin,
    enable_captcha=True,
    login_logo_url="https://preview.tabler.io/static/logo.svg"
)



def create_app():
    app_fastapi = FastAPI()
    app_fastapi.mount(
        '/static',
        StaticFiles(directory=os.path.join(BASE_DIR, "static")),
        name="static",
    )
    app_fastapi.mount("/admin", admin_app)
    app_fastapi.include_router(staff.router)

    @app_fastapi.get('/')
    def root():
        return {'message': 'It`s a root endpoint!'}

    @admin_app.register
    class Home(Link):
        label = "Home"
        icon = "fas fa-home"
        url = "/admin"    
    return app_fastapi
