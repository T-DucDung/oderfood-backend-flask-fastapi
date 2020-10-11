import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler  # other schedulers are available
from fastapi import FastAPI
from fastapi_sqlalchemy import db

from app.models import User, UserCount

app = FastAPI()

MYSQL_HOST = '172.17.0.2'
MYSQL_NAME = 'test'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123'

app.add_middleware(DBSessionMiddleware, db_url="mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
    DB_USER=MYSQL_USER,
    DB_PASS=MYSQL_PASSWORD,
    DB_ADDR=MYSQL_HOST,
    DB_NAME=MYSQL_NAME))


@app.on_event('startup')
async def startup_event():
    scheduler = AsyncIOScheduler(timezone=pytz.utc)
    scheduler.start()
    scheduler.add_job(count_users_task, "cron", hour=0)  # runs every night at midnight