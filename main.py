from fastapi import FastAPI
from database import database
from routers import categories, order_items, orders, products, users

app = FastAPI(
    title="FastAPI",
    description="API",
    version="1.0.0"
)

app.include_router(products.router)
app.include_router(orders.router)
app.include_router(users.router)
app.include_router(order_items.router)
app.include_router(categories.router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()