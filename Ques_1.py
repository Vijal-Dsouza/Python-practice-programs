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

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Employees (
        ID INT PRIMARY KEY,
        Name VARCHAR(100),
        Age INT,
        Department VARCHAR(100)
    )
    '''

    cursor.execute(create_table_query)
    print("Employees Table created successfully.")

    insert_query = " INSERT INTO Employees (ID, Name, Age, Department) VALUES (%s, %s, %s, %s) "
    values = [
        (1, 'Alice', 30, 'HR'),
        (2, 'Bob', 25, 'Engineering'),
        (3, 'Charlie', 28, 'Marketing')
    ]

    cursor.executemany(insert_query, values)
    cursor.commit()
    print("Records inserted successfully.")

    cursor.execute("SELECT * FROM Employees")
    for row in cursor.fetchall():
        print(row)

except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
except Exception as e:
        print(f"Unexpected Error: {e}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")