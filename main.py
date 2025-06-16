from fastapi import FastAPI
from database import database
from routers import categories, order_items, orders, products, users

app = FastAPI(
    title="FastAPI",
    description="API",
    version="1.0.0",
)

app.include_router(products.router)
app.include_router(orders.router)
app.include_router(users.router)
app.include_router(order_items.router)
app.include_router(categories.router)


@app.get("/", tags=["root"])
async def read_root() -> dict[str, str]:
    """Simple health check endpoint."""
    return {"message": "API is running"}


@app.on_event("startup")
async def startup() -> None:
    await database.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await database.disconnect()

