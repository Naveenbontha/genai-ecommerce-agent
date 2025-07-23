import sqlite3

def run_query(sql_query: str):
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    try:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        result = [dict(zip(column_names, row)) for row in rows]
    except Exception as e:
        result = {"error": str(e)}

    conn.close()
    return result
