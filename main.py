from fastapi import FastAPI
from Backend.routes import products, orders, cart, chatbot
from fastapi.staticfiles import StaticFiles
import os
import uvicorn
import logfire

app = FastAPI()

#config for observability
logfire.configure(send_to_logfire="if-token-present")
logfire.instrument_fastapi(app)
logfire.instrument_pydantic()

#create uoload images for product image
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
#Include api routes
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(cart.router)
app.include_router(chatbot.router)

#serve uploaded files statically
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


# Serve Frontend natively
app.mount("/", StaticFiles(directory="Frontend", html=True), name="frontend")

if __name__ == "__main__":
    print("🔍Starting server on port 8000...")
    uvicorn.run(app, host="0.0.0.0", port=8000)