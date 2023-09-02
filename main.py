from fastapi import FastAPI
from database.db import Base, engine
from routers.item.logic.items import item_router

Base.metadata.create_all(bind= engine)

app = FastAPI(title="FastApi_Project")

app.include_router(
    item_router
    )