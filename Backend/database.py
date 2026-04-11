"""
Database configuration and MongoDB connection setup
"""

from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

MONGO_URI = os.getenv("MONGO_URI")


client = MongoClient(MONGO_URI)
db = client["ecommerce_db"]

#collection
user_collection= db['users']
product_collection = db['products']
order_collection = db['orders']
cart_collection = db['cart']


