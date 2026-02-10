from fastapi import FastAPI
from models import Sale
import crud

app = FastAPI(title="Data Backend API")


@app.get("/sales")
def list_sales(limit: int = 10, offset: int = 0):
    items = crud.get_sales(limit, offset)
    return {
        "items": items,
        "limit": limit,
        "offset": offset,
        "count": len(items)
    }


@app.get("/sales/customer/{customer_id}")
def sales_by_customer(customer_id: str):
    items = crud.get_sales_by_customer(customer_id)
    return {
        "items": items,
        "count": len(items)
    }


@app.get("/sales/category/{category}")
def sales_by_category(category: str, limit: int = 10, offset: int = 0):
    items = crud.get_sales_by_category(category, limit, offset)
    return {
        "items": items,
        "limit": limit,
        "offset": offset,
        "count": len(items)
    }


@app.post("/sales")
def create_sale(sale: Sale):
    crud.add_sale(sale)
    return {"message": "Sale added successfully"}
