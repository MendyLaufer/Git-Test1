class Employee:

    def __init__(self, employee_id: int, role_id: int, manager_id: int, first_name: str, middle_name: str,
                 last_name: str, email_address: str, phone_number: str, hire_date: str, salary: float):
        self.employee_id = employee_id
        self.role_id = role_id
        self.manager_id = manager_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.hire_date = hire_date
        self.salary = salary

    def set_role_id(self, role_id: int):
        self.role_id = role_id

    def set_manager_id(self, manager_id: int):
        self.manager_id = manager_id

    def update_phone(self, phone_number: str):
        self.phone_number = phone_number

    def set_salary(self, salary: float):
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.employee_id}\nRole ID: {self.role_id}\nManager ID: {self.manager_id}\n" \
               f"First Name: {self.first_name}\nMiddle Name: {self.middle_name}\nLast Name: {self.last_name}\n" \
               f"Email Address: {self.email_address}\nPhone Number: {self.phone_number}\nHire Date: {self.hire_date}\n" \
               f"Salary: {self.salary}"




