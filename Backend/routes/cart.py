"""
Shopping cart routes for adding and retrieving items.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from Backend.models import CartItem
from ..database import cart_collection

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.post("/add")
async def add_to_cart(item: CartItem):
    """
    Add an item to the user's cart.
    """
    item_data =item.model_dump() if hasattr(item, "model_dump") else item.model_dump()
    cart_collection.insert_one(item_data)
    return {"message": "Item added to cart successfully"}

@router.get("/{user_email}")
async def get_cart(user_email: str):
    """
    Get all items in the user's cart.
    """
    cart_items = list(cart_collection.find({"user_email": user_email},{"_id": 0}))
    return cart_items

@router.delete("/{user_email}")
async def clear_cart(user_email: str):
    """
    Clear all items in the user's cart.
    """
    cart_collection.delete_many({"user_email": user_email})
    return {"message": "Cart cleared successfully"}

