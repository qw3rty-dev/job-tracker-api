from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import init_db,get_connection
from routes import jobs
import threading
import time
from scraper import run_scraper_once
from sqlite3 import IntegrityError


def background_scraper():
    while True:
        run_scraper_once()
        time.sleep(600)


@asynccontextmanager
async def lifespan(app: FastAPI):
    
    thread= threading.Thread(target=background_scraper)
    thread.daemon= True
    thread.start()
    yield
    print("App shutting down....")


app= FastAPI(lifespan=lifespan)
init_db()
app.include_router(jobs.router)
