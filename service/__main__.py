from fastapi import FastAPI
import uvicorn

from service import config
from service.routers import staff
#from service.worker import source

app_config = config.load_from_env()


if __name__ == '__main__':
    uvicorn.run('service.app:create_app', port=5000, reload=True, access_log=False)
