from pathlib import Path

#curent_dir = Path().cwd()
env_file = Path().cwd() / '.env'


def get_dir():
    with open(env_file, 'r') as config:
        text = config.readlines()
    return text
