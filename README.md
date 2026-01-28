# Data Backend API

## Overview
This project implements a RESTful backend service that exposes sales data
stored in a relational database. The API supports querying, filtering,
pagination, and insertion of records.

## Endpoints
- GET /sales?limit=&offset=
- GET /sales/customer/{customer_id}
- POST /sales

## Architecture
- FastAPI for API layer
- SQLite for persistence
- Modular CRUD-based design

## How to Run
```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
