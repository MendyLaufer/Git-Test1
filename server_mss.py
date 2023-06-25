import pyodbc

driver_name = 'SQL Server'
server_name = 'EVYATAR'
db_name = 'employee_db'

conn_str = f"DRIVER={{{driver_name}}};SERVER={server_name};DATABASE={db_name};Trusted_Connection=yes;"

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

query = 'SELECT * FROM Employee'  # Replace 'TableName' with the actual table name

cursor.execute(query)

for row in cursor:
    print(row)

cursor.close()
conn.close()