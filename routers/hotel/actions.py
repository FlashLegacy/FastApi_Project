from fastapi import APIRouter


hotel_router = APIRouter(
    prefix="/hotel",
    tags=["Hotel"]
)

@hotel_router.get("/hello", status_code= 200)
async def say_hello():
    return {
        "message": "Hello world!"
    }