import pytz

from apscheduler.schedulers.asyncio import AsyncIOScheduler  # other schedulers are available
from fastapi import FastAPI
from fastapi_sqlalchemy import db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

MYSQL_HOST = 'localhost'
MYSQL_NAME = 'test'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'Nguyenvanvu17150217'


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
    DB_USER=MYSQL_USER,
    DB_PASS=MYSQL_PASSWORD,
    DB_ADDR=MYSQL_HOST,
    DB_NAME=MYSQL_NAME)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@app.on_event('startup')
async def startup_event():
    scheduler = AsyncIOScheduler(timezone=pytz.utc)
    scheduler.start()
    # scheduler.add_job(count_users_task, "cron", hour=0)  # runs every night at midnight