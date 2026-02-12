# Data Backend API

## Overview
This project implements a RESTful backend service that exposes sales data
stored in a relational database. The API supports querying, filtering,
pagination, and insertion of records.

Paginated endpoints return metadata such as limit, offset, and item count
to help clients manage large result sets.

## Endpoints
- GET /sales?limit=&offset=
- GET /sales/customer/{customer_id}
- GET /sales/category/{category}?limit=&offset=
- POST /sales

## Architecture
- FastAPI for API layer
- SQLite for persistence
- Modular CRUD-based design
- Pagination metadata included in API responses

## Design Decisions

- Used FastAPI for its lightweight structure and automatic OpenAPI documentation.
- Chose SQLite for simplicity and easy local development.
- Implemented pagination to prevent large payload responses.
- Added filtering endpoints to keep API flexible and scalable.
- Separated CRUD logic from API routes to maintain clean architecture.


## How to Run
```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
