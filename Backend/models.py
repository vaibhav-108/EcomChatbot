"""
Pydantic models for validations and serializations
"""

from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from enum import Enum
from datetime import datetime


class Product(BaseModel):
    "Product model for base inventory"
    name: str
    description: str
    price: int
    category: str
    size: List[str] #S, M, L, XL, XXL
    color: List[str]  #red, blue, black etc
    image: str  #url for picsum photos
    
class Order(BaseModel):
    "Order model for customer orders"
    user_email: EmailStr
    product_name: str
    quantity: int
    
class CartItem(BaseModel):
    "Cart model for customer cart items"
    user_email: str
    product_name: str
    quantity: int