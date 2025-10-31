import mysql.connector
try:
    conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="testdb",
            use_pure=True
        )

    cursor = conn.cursor()

    read_query = "SELECT * FROM employees"
    cursor.execute(read_query)

    def batch_processing():
        while True:
            rows = cursor.fetchmany(size=500)
            if not rows:
                break
            for row in rows:
                yield row
    for row in batch_processing():
        print(*row)
    
except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
except Exception as e:
        print(f"Unexpected Error: {e}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")