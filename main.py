from fastapi import FastAPI, APIRouter
from database import database
from routers import categories, order_items, orders, products, users

app = FastAPI(
    title="FastAPI",
    description="API",
    version="1.0.0"
)

api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(products.router)
api_v1.include_router(orders.router)
api_v1.include_router(users.router)
api_v1.include_router(order_items.router)
api_v1.include_router(categories.router)

app.include_router(api_v1)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()