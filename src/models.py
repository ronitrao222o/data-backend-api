from pydantic import BaseModel
from datetime import date

class Sale(BaseModel):
    order_id: int
    customer_id: str
    product: str
    category: str
    order_date: date
    quantity: int
    price: float
