from server_mss import SqlQuery


class HrManagement:

    def __init__(self):
        self.db = SqlQuery()

    def get_employee(self, employee_id):
        query = f"SELECT * FROM employee WHERE employee_id = {employee_id}"
        self.db.query_select(query)

    def add_employee(self, employee):
        query = f"INSERT INTO employee (employee_id, role_id, first_name, last_name, email_address, phone_number, hire_date, salary ,department_id, hub_id) VALUES ({employee.employee_id}, {employee.role_id}, '{employee.first_name}', '{employee.last_name}', '{employee.email_address}', '{employee.phone_number}', '{employee.hire_date}', {employee.salary}, {employee.department_id}, {employee.hub_id})"
        self.db.query_set(query)

    def delete_employee(self, employee_id):
        query = f"DELETE FROM employee WHERE employee_id = {employee_id}"
        self.db.query_set(query)

    def set_role_id(self, employee_id: int, role_id: int):
        query = f"UPDATE employee SET role_id = {role_id} WHERE employee_id = {employee_id}"
        self.db.query_set(query)

    def update_phone(self, employee_id: int, phone_number: str):
        query = f"UPDATE employee SET phone_number = '{phone_number}' WHERE employee_id = {employee_id}"
        self.db.query_set(query)

    def set_salary(self, employee_id: int, salary: float):
        query = f"UPDATE employee SET salary = {salary} WHERE employee_id = {employee_id}"
        self.db.query_set(query)

    def set_department_id(self, employee_id: int, department_id: int):
        query = f"UPDATE employee SET department_id = {department_id} WHERE employee_id = {employee_id}"
        self.db.query_set(query)

    def set_hub_id(self, employee_id: int, hub_id: int):
        query = f"UPDATE employee SET hub_id = {hub_id} WHERE employee_id = {employee_id}"
        self.db.query_set(query)

    def general_employees_sum(self):
        query = "SELECT SUM (salary) FROM employee"
        self.db.query_select(query)






