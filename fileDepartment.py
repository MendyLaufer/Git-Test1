from server_mss import SqlQuery


class Department:
    def __init__(self, department_id=0, department_name=0, manager_id=0, hub_id=0):
        self.department_id = department_id
        self.department_name = department_name
        self.manager_id = manager_id
        self.hub_id = hub_id
        self.db = SqlQuery()

    def set_manager_id(self, manager_id):
        query = f"SELECT * FROM MANAGER WHERE employee_id = {manager_id}"
        self.db.cursor1.execute(query)
        manager_row = self.db.cursor1.fetchone()

        if manager_row:
            self.manager_id = manager_id
            query = f"UPDATE Department SET manager_id = {manager_id} WHERE department_id = {self.department_id}"
            self.db.query_set(query)
            print("Manager ID updated successfully.")
        else:
            print("Invalid manager ID. Please provide an existing manager ID.")




