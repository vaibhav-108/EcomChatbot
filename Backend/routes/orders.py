"""
Orders manament routes for placing new orders.
"""

from fastapi import APIRouter
from Backend.models import Order
from ..database import order_collection

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("")
async def place_order(order: Order):
    """
    Place a new order.
    """
    order_data = order.model_dump() if hasattr(order, "model_dump") else order.model_dump()
    order_collection.insert_one(order_data)
    return {"message": "Order placed successfully"}



