from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    hashed_password: str
    created_at: str

class UsersResponse(BaseModel):
    users: List[User]
    total: int

class Category(BaseModel):
    id: int
    name: str
    description: str | None

class CategoriesResponse(BaseModel):
    categories: List[Category]
    total: int

class Product(BaseModel):
    id: int
    name: str
    description: str | None
    price: float
    category_id: int
    stock: int
    created_at: str

class ProductsResponse(BaseModel):
    products: List[Product]
    total: int

class Order(BaseModel):
    id: int
    user_id: int
    order_date: str
    status: str
    total_amount: float

class OrdersResponse(BaseModel):
    orders: List[Order]
    total: int

class OrderItem(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    unit_price: float

class OrderItemsResponse(BaseModel):
    order_items: List[OrderItem]
    total: int