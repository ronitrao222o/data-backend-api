from fastapi import FastAPI
from models import Sale
import crud
import sqlite3

app = FastAPI(title="Data Backend API")

@app.get("/sales")
def list_sales(limit: int = 10, offset: int = 0):
    return crud.get_sales(limit, offset)


@app.get("/sales/customer/{customer_id}")
def sales_by_customer(customer_id: str):
    return crud.get_sales_by_customer(customer_id)


@app.post("/sales")
def create_sale(sale: Sale):
    crud.add_sale(sale)
    return {"message": "Sale added successfully"}
