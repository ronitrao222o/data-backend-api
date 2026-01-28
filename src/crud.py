from database import get_connection

def get_sales(limit=10, offset=0):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM sales
        LIMIT ? OFFSET ?
    """, (limit, offset))

    rows = cursor.fetchall()
    conn.close()
    return rows


def get_sales_by_customer(customer_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM sales WHERE customer_id = ?
    """, (customer_id,))

    rows = cursor.fetchall()
    conn.close()
    return rows


def add_sale(sale):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sales
        (order_id, customer_id, product, category, order_date, quantity, price)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        sale.order_id,
        sale.customer_id,
        sale.product,
        sale.category,
        sale.order_date,
        sale.quantity,
        sale.price
    ))

    conn.commit()
    conn.close()
