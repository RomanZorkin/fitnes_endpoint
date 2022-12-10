import uvicorn

from service.app import app1

app = app1()

if __name__ == '__main__':   
    #uvicorn.run('__main__:app', port=5000, reload=True, access_log=False)
    app1()