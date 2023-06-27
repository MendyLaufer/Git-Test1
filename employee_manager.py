from server_mss import SqlQuery

class EmployeeManager:
    pass
    def __init__(self):
        self.db = SqlQuery()

    def set_role_id(self, employee_id: int, role_id: int):
        query = f"UPDATE employee SET role_id = {role_id} WHERE employee_id = {employee_id}"
        self.db.query_set(query)

    def set_manager_id(self, employee_id: int, manager_id: int):
        query = f"UPDATE employee SET manager_id = {manager_id} WHERE employee_id = {employee_id}"
        self.db.query_set(query)

    def update_phone(self, employee_id: int, phone_number: str):
        query = f"UPDATE employee SET phone_number = '{phone_number}' WHERE employee_id = {employee_id}"
        self.db.query_set(query)

    def set_salary(self, employee_id: int, salary: float):
        query = f"UPDATE employee SET salary = {salary} WHERE employee_id = {employee_id}"
        self.db.query_set(query)

    def __str__(self):
        query = f"SELECT * FROM employee WHERE employee_id = {self.employee_id}"
        self.db.query_select(query)
