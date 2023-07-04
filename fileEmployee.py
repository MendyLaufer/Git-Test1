from server_mss import SqlQuery


class Employee:
    counter = 0

    def __init__(self, employee_id: int = None, role_id: int = None, first_name: str = None, last_name: str = None,
                 email_address: str = None, phone_number: str = None, hire_date: str = None, salary: float = None,
                 department_id: int = None, hub_id: int = None):
        if employee_id is None:
            Employee.counter += 1
            self.employee_id = Employee.counter
        else:
            self.employee_id = employee_id

        self.role_id = role_id
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.hire_date = hire_date
        self.department_id = department_id
        self.hub_id = hub_id
        self.salary = salary

        self.db = SqlQuery()

        if self.role_id is not None:
            query = f"SELECT min_salary, max_salary FROM Role WHERE role_id = {self.role_id}"
            self.db.query_select(query)
            role_row = self.db.cursor.fetchone()

            if role_row:
                min_salary = role_row.min_salary
                max_salary = role_row.max_salary

                if salary is not None:
                    self.salary = max(min(salary, max_salary), min_salary)
                else:
                    self.salary = min_salary

    def is_employee_exists(self, employee_id: int) -> bool:
        query = f"SELECT employee_id FROM employee WHERE employee_id = {employee_id}"
        self.db.query_select(query)
        employee_row = self.db.cursor.fetchone()
        return employee_row is not None

    def set_salary(self, employee_id: int, salary: float):
        if self.is_employee_exists(employee_id):
            role_query = f"SELECT min_salary, max_salary FROM Role WHERE role_id = {self.role_id}"
            self.db.query_select(role_query)
            role_row = self.db.cursor.fetchone()

            if role_row:
                min_salary = role_row.min_salary
                max_salary = role_row.max_salary

                if salary < min_salary:
                    salary = min_salary
                elif salary > max_salary:
                    salary = max_salary

                query = f"UPDATE employee SET salary = {salary} WHERE employee_id = {employee_id}"
                self.db.query_set(query)
                print("Salary updated successfully.")
            else:
                print("Failed to update salary. Invalid role ID.")
        else:
            print("Failed to update salary. Invalid employee ID.")

    def update_phone(self, employee_id: int, phone_number: str):
        query = f"UPDATE employee SET phone_number = '{phone_number}' WHERE employee_id = {employee_id}"
        self.db.query_set(query)

    def set_role_id(self, employee_id: int, role_id: int):
        if self.is_employee_exists(employee_id):
            role_query = f"SELECT role_id FROM Role WHERE role_id = {role_id}"
            self.db.query_select(role_query)
            role_row = self.db.cursor.fetchone()

            if role_row:
                query = f"UPDATE employee SET role_id = {role_id} WHERE employee_id = {employee_id}"
                self.db.query_set(query)
                print("Role ID updated successfully.")
            else:
                print("Failed to update role ID. Invalid role ID.")
        else:
            print("Failed to update role ID. Invalid employee ID.")

    def set_department_id(self, employee_id: int, department_id: int):
        if self.is_employee_exists(employee_id):
            department_query = f"SELECT department_id FROM department WHERE department_id = {department_id}"
            self.db.query_select(department_query)
            department_row = self.db.cursor.fetchone()

            if department_row:
                query = f"UPDATE employee SET department_id = {department_id} WHERE employee_id = {employee_id}"
                self.db.query_set(query)
                print("Department ID updated successfully.")
            else:
                print("Failed to update department ID. Invalid department ID.")
        else:
            print("Failed to update department ID. Invalid employee ID.")

    def set_hub_id(self, employee_id: int, hub_id: int):
        query = f"UPDATE employee SET hub_id = {hub_id} WHERE employee_id = {employee_id}"
        self.db.query_set(query)
