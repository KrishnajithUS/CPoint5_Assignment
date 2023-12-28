from pydantic import BaseModel

class InventoryItemCreate(BaseModel):
    name: str
    category: str
    quantity_in_stock: int = 0
    price_per_unit: float  = 0
    supplier_name: str
    contact_info:str
    
class InventoryItemResponse(BaseModel):
    id: int
    name: str
    category: str
    quantity_in_stock: int
    price_per_unit: float
    supplier_name: str
    contact_info:str
    
    class Config:
        from_attributes = True
