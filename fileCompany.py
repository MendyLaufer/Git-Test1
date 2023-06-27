from fileEmployee import Employee
from server_mss import SqlQuery
from employee_manager import EmployeeManager


class Company:
    def __init__(self, ceo_name, cto_name, cfo_name):
        self.ceo_name = ceo_name
        self.cto_name = cto_name
        self.cfo_name = cfo_name
        self.db = SqlQuery()

    def add_employee(self, employee):
        query = f"INSERT INTO employee (employee_id, role_id, first_name, last_name, email_address, phone_number, hire_date, salary ,department_id, hub_id) VALUES ({employee.employee_id}, {employee.role_id}, '{employee.first_name}', '{employee.last_name}', '{employee.email_address}', '{employee.phone_number}', '{employee.hire_date}', {employee.salary}, {employee.department_id}, {employee.hub_id})"
        self.db.query_set(query)

    def update_employee(self, employee):
        query = f"UPDATE employee SET role_id = {employee.role_id},  first_name = '{employee.first_name}', last_name = '{employee.last_name}', email_address = '{employee.email_address}', phone_number = '{employee.phone_number}', hire_date = '{employee.hire_date}', salary = {employee.salary} WHERE employee_id = {employee.employee_id}"
        self.db.query_set(query)

    def delete_employee(self, employee_id):
        query = f"DELETE FROM employee WHERE employee_id = {employee_id}"
        self.db.query_set(query)

    def get_employee(self, employee_id):
        query = f"SELECT * FROM employee WHERE employee_id = {employee_id}"
        self.db.query_select(query)

    def general_employees_sum(self):
        query = "SELECT SUM (salary) FROM employee"
        self.db.query_select(query)




# company = Company("CEO Name", "CTO Name", "CFO Name")
# employee = Employee(209,  1, "John", "Doe", "john@example.com", "123456789", "2023-06-27", 5000.0)
# employee.set_hub_id()
