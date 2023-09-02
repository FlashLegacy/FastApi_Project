from fastapi import FastAPI
from routers.item.logic.items import item_router

app = FastAPI(title="FastApi_Project")

app.include_router(
    item_router
    )