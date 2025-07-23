from fastapi import FastAPI
from database.database import engine
from database import database
from model_loader import *  # Make sure this imports all models
from controllers import order

app = FastAPI()

database.Base.metadata.create_all(bind=engine)

app.include_router(order.router)
