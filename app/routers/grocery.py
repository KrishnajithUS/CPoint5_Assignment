from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..models import models,schemas,database
from typing import List


router = APIRouter()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/grocery/", tags=["grocery"],response_model=schemas.InventoryItemResponse)
async def add_grocery(grocery: schemas.InventoryItemCreate, db: Session = Depends(get_db)):
    inventory = models.InventoryItem(**grocery.model_dump())
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory
  
@router.get("/grocery/", tags=["grocery"],response_model=List[schemas.InventoryItemResponse])
async def list_grocery(db:Session = Depends(get_db)):
    return db.query(models.InventoryItem).all()