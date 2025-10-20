import sqlite3
import json
import random

def get_all_orders():
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            *
        FROM Orders o
        """
        )
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        orders = []
        for row in query_results:
            orders.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_orders = json.dumps(orders)

    return serialized_orders

def get_single_order(pk):
    with sqlite3.connect("./kneeldiamonds.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            *
        FROM Orders o
        WHERE o.id = ?
        """, (pk,))
        query_results = db_cursor.fetchone()

        # Serialize Python list to JSON encoded string
        serialized_order = json.dumps(dict(query_results))

    return serialized_order

def create_order(order_data):
    with sqlite3.connect("./kneeldiamonds.db") as conn:    
        # Query docks directly from the database
        db_cursor = conn.cursor()
        db_cursor.execute("SELECT id FROM Orders")

        db_cursor.execute(
            """
            INSERT INTO Orders (metal_id, style_id, size_id)
            VALUES (?, ?, ?)
            """,
            (order_data['metal_id'], order_data['style_id'], order_data['size_id'])
        )
        new_id = db_cursor.lastrowid
        conn.commit()

    return new_id if new_id else False

def delete_order(pk):
    with sqlite3.connect("./kneeldiamonds.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Orders WHERE id = ?
        """, (pk,)
        )
        number_of_rows_deleted = db_cursor.rowcount
    return True if number_of_rows_deleted > 0 else False