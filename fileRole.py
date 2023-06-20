class Role:
    def __init__(self, role_id, role_name, max_salary, min_salary):
        self.role_id = role_id
        self.role_name = role_name
        self.max_salary = max_salary
        self.min_salary = min_salary

    def setMax_salary(self, max_salary):
        self.max_salary = max_salary

    def setMin_salary(self, min_salary):
        self.min_salary = min_salary

    def __str__(self):
        return f"Role ID: {self.role_id}, Role Name: {self.role_name}, Max Salary: {self.max_salary}, Min Salary: {self.min_salary}"
