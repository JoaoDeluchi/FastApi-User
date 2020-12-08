from fastapi import FastAPI
from domain.user.views import router as user_routers
from config.db import start_db

def create_app():
    app = FastAPI()
    app.include_router(user_routers, prefix="/user", tags=["Users Management"])
    start_db()
    return app
