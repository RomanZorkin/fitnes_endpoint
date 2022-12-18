# fitnes_endpoint
simple API fitness service
#
## Instalation

```bash
python -m venv venv

source venv/bin/activate

pip install poetry

poetry install
```
#
## You need create .env file with rules:
```
# APP settings
APP_HOST=0.0.0.0
APP_PORT=1300

# 1C endpoint settings. Use only if DB not work
ENDPOINT=http://176.192.70.122:90/fitnes_t_nfc_mobile/hs/nfc_mobile/v1
USER=FitnessKit
PASSWORD=vY0xodyg

DATABASE_URL=postgresql+asyncpg://vasy:123@db:5432/
```
#
## Before we start our service we need start admin service + db

Instructions in 




## than you can start
```
make run
```