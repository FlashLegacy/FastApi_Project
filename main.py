from fastapi import FastAPI
from routers.hotel.actions import hotel_router

app = FastAPI(
    title="MainApp",
)

app.include_router(hotel_router)