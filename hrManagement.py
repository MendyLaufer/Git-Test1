from server_mss import SqlQuery
from fileEmployee import Employee
from fileManager import Manager


class HrManagement:
    def __init__(self):
        self.db = SqlQuery()

    def add_manager(self, manager: Manager):
        self.add_employee(manager)
        print("Manager added successfully.")

    def add_employee(self, employee: Employee):
        # if employee.employee_id is None:
        #     employee.employee_id = self.generate_employee_id()
        query = f"INSERT INTO employee (employee_id, role_id, first_name, last_name, email_address," \
                f" phone_number, hire_date, salary, department_id, hub_id) " \
                f"VALUES ({employee.employee_id}, {employee.role_id}, '{employee.first_name}', '{employee.last_name}'," \
                f"'{employee.email_address}', '{employee.phone_number}', '{employee.hire_date}', {employee.salary}," \
                f" {employee.department_id}, {employee.hub_id})"
        self.db.query_set(query)
        print("Employee added successfully.")

    def delete_employee(self, employee_id):
        query = f"DELETE FROM employee WHERE employee_id = {employee_id}"
        self.db.query_set(query)


    def general_employees_sum(self):
        query = "SELECT SUM (salary) FROM employee"
        self.db.query_select(query)

    def get_employee(self, employee_id: int):
        query = f"SELECT * FROM employee WHERE employee_id = {employee_id}"
        self.db.query_select(query)
        employee_row = self.db.cursor.fetchone()

        if employee_row:
            print(employee_row)
        else:
            print("Employee not found.")
    def set_hub_manager_id(self, manager_id, hub_id):
        query = f"UPDATE hub SET manager_id = {manager_id} WHERE hub_id = {hub_id}"
        self.db.query_set(query)
        print("Hub manager ID updated successfully.")

    def add_department(self, department_id, department_name):
        query = f"INSERT INTO department (department_id, department_name) VALUES ({department_id}, '{department_name}')"
        self.db.query_set(query)
        print("Department added successfully.")

    def remove_department(self, department_id):
        query = f"DELETE FROM department WHERE department_id = {department_id}"
        self.db.query_set(query)
        print("Department removed successfully.")





