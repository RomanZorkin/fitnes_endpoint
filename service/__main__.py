import uvicorn

from service import config

app_config = config.load_from_env().host

if __name__ == '__main__':
    uvicorn.run(
        'service.app:create_app',
        host=app_config.app_host,
        port=app_config.app_port,
        reload=True,
        access_log=False,
    )
