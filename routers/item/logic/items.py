from fastapi import APIRouter

item_router = APIRouter(
    prefix = "/Items"
)


@item_router.get("/item/hello", status_code= 200)
async def say_hello():
    return {
        "message": "Hello world!"
    }
