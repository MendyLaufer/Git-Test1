import pyodbc


class SqlQuery:
    def __init__(self):
        self.driver_name = 'SQL Server'
        self.server_name = 'Evyatar\SQLEXPRESS01'
        self.db_name = 'HR_DB'
        self.conn = None
        self.cursor1 = None

    def connect(self):
        conn_str = f"DRIVER={{{self.driver_name}}};SERVER={self.server_name};DATABASE={self.db_name};Trusted_Connection=yes;"
        self.conn = pyodbc.connect(conn_str)
        self.cursor1 = self.conn.cursor()

    def close_connection(self):
        if self.cursor1:
            self.cursor1.close()
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def query_set(self, query):
        self.connect()
        self.cursor1.execute(query)
        self.conn.commit()
        self.close_connection()

    def query_select(self, query):
        self.connect()
        self.cursor1.execute(query)
        for row in self.cursor1:
            print(row)
        self.close_connection()






