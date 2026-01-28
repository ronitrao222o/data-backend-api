CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER PRIMARY KEY,
    customer_id TEXT,
    product TEXT,
    category TEXT,
    order_date DATE,
    quantity INTEGER,
    price REAL
);
