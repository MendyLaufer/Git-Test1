from server_mss import SqlQuery


class Employee:


    def __init__(self,employee_id: int, role_id: int, first_name: str, last_name: str,
                 email_address: str, phone_number: str, hire_date: str, salary: float, department_id: int, hub_id: int):
        self.employee_id = employee_id
        self.role_id = role_id
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.hire_date = hire_date
        self.salary = salary
        self.department_id = department_id
        self.hub_id = hub_id     
        self.db = SqlQuery()

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
        
    def __str__(self):
        query = f"SELECT * FROM employee WHERE employee_id = {self.employee_id}"
        self.db.query_select(query)





