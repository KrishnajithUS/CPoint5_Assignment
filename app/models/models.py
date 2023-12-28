from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Float
from sqlalchemy.orm import relationship

from .database import Base


class InventoryItem(Base):
    __tablename__ = "Inventory"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String)
    quantity_in_stock = Column(Integer)
    price_per_unit = Column(Float)
    supplier_name = Column(String)
    contact_info = Column(String)
 