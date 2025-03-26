import os
import datetime
from sqlalchemy import Table, Column, ForeignKey, Float, Integer, String, DateTime, MetaData, create_engine

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
DB_PATH = os.path.join(BASE_DIR, "test.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

print("↪ [INIT_DB] BASE_DIR     =", BASE_DIR)
print("↪ [INIT_DB] DB_PATH       =", DB_PATH)
print("↪ [INIT_DB] USING URL     =", DATABASE_URL)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), nullable=False, unique=True),
    Column("email", String(100), nullable=False, unique=True),
    Column("full_name", String(100), nullable=False),
    Column("hashed_password", String(255), nullable=False),
    Column("created_at", DateTime, default=datetime.datetime.utcnow)
)

categories = Table(
    "categories", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False, unique=True),
    Column("description", String(255), nullable=True)
)

products = Table(
    "products", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("description", String(500), nullable=True),
    Column("price", Float, nullable=False),
    Column("category_id", Integer, ForeignKey("categories.id"), nullable=False),
    Column("stock", Integer, nullable=False, default=0),
    Column("created_at", DateTime, default=datetime.datetime.utcnow)
)

orders = Table(
    "orders", metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
    Column("order_date", DateTime, default=datetime.datetime.utcnow),
    Column("status", String(20), nullable=False, default="pending"),
    Column("total_amount", Float, nullable=False, default=0.0)
)

order_items = Table(
    "order_items", metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", Integer, ForeignKey("orders.id"), nullable=False),
    Column("product_id", Integer, ForeignKey("products.id"), nullable=False),
    Column("quantity", Integer, nullable=False),
    Column("unit_price", Float, nullable=False)
)

metadata.create_all(engine)

with engine.begin() as conn:
    conn.execute(users.insert(), [
        {
            "username": "alice",
            "email": "alice@example.com",
            "full_name": "Alice Wonderland",
            "hashed_password": "fakehashedpassword1"
        },
        {
            "username": "bob",
            "email": "bob@example.com",
            "full_name": "Bob Builder",
            "hashed_password": "fakehashedpassword2"
        }
    ])

    conn.execute(categories.insert(), [
        {"name": "Electronics", "description": "Gadgets, phones, and accessories"},
        {"name": "Books", "description": "Printed and digital books"}
    ])

    conn.execute(products.insert(), [
        {
            "name": "Smartphone Model X",
            "description": "Latest generation smartphone with OLED display",
            "price": 799.99,
            "category_id": 1,
            "stock": 50
        },
        {
            "name": "Wireless Earbuds",
            "description": "Noise-cancelling wireless earbuds",
            "price": 129.50,
            "category_id": 1,
            "stock": 200
        },
        {
            "name": "Learn Python Book",
            "description": "An introductory book on Python programming",
            "price": 39.95,
            "category_id": 2,
            "stock": 100
        },
        {
            "name": "Advanced SQL Guide",
            "description": "Deep dive into SQL and database design",
            "price": 49.90,
            "category_id": 2,
            "stock": 75
        }
    ])

    conn.execute(orders.insert(), [
        {
            "user_id": 1,
            "order_date": datetime.datetime(2025, 6, 1, 14, 30),
            "status": "completed",
            "total_amount": 929.49
        },
        {
            "user_id": 2,
            "order_date": datetime.datetime(2025, 6, 2, 10, 15),
            "status": "pending",
            "total_amount": 39.95
        }
    ])

    conn.execute(order_items.insert(), [
        {
            "order_id": 1,
            "product_id": 1,
            "quantity": 1,
            "unit_price": 799.99
        },
        {
            "order_id": 1,
            "product_id": 2,
            "quantity": 1,
            "unit_price": 129.50
        },
        {
            "order_id": 2,
            "product_id": 3,
            "quantity": 1,
            "unit_price": 39.95
        }
    ])

print("Dummy tables and records created successfully.")