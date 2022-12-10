from service import config
from service.worker import source

app_config = config.load_from_env()


def app():
    team = source.get_team()
    print('hello', '\n', team)

