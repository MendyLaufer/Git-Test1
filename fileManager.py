from server_mss import SqlQuery
from fileEmployee import Employee


class Manager(Employee):
    def __init__(self, manager_id, role_id=None, first_name=None, last_name=None, email_address=None,
                 phone_number=None, hire_date=None, salary=None, department_id=None, hub_id=None,
                 employee_id=None):
        super().__init__(role_id, first_name, last_name, email_address, phone_number, hire_date, salary,
                         department_id, hub_id, employee_id)
        self.manager_id = manager_id
        self.db = SqlQuery()

    def update_manager_details(self, role_id=None, first_name=None, last_name=None, email_address=None,
                               phone_number=None, hire_date=None, salary=None, department_id=None, hub_id=None):
        if role_id:
            self.set_role_id(self.manager_id, role_id)
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email_address:
            self.email_address = email_address
        if phone_number:
            self.update_phone(self.manager_id, phone_number)
        if hire_date:
            self.hire_date = hire_date
        if salary:
            self.set_salary(self.manager_id, salary)
        if department_id:
            self.set_department_id(self.manager_id, department_id)
        if hub_id:
            self.set_hub_id(self.manager_id, hub_id)

        query = f"UPDATE managers SET role_id = {self.role_id}, first_name = '{self.first_name}', last_name = '{self.last_name}', " \
                f"email_address = '{self.email_address}', phone_number = '{self.phone_number}', hire_date = '{self.hire_date}', " \
                f"salary = {self.salary}, department_id = {self.department_id}, hub_id = {self.hub_id}, " \
                f"employee_id = {self.employee_id} WHERE manager_id = {self.manager_id}"
        self.db.query_set(query)

    def set_department_id_manager(self, employee_id: int, department_id: int):
        super().set_department_id(employee_id, department_id)
        query = f"UPDATE managers SET department_id = {department_id} WHERE manager_id = {employee_id}"
        self.db.query_set(query)

    def set_hub_id_manager(self, employee_id: int, hub_id: int):
        super().set_hub_id(employee_id, hub_id)
        query = f"UPDATE managers SET hub_id = {hub_id} WHERE manager_id = {employee_id}"
        self.db.query_set(query)
