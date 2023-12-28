from fastapi import Depends, FastAPI
from .routers import grocery
from .models import models,schemas,database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(grocery.router)
