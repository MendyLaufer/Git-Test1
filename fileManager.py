from fileEmployee import Employee


class Manager(Employee):
    def __init__(self, manager_id: int = None, role_id: int = None, first_name: str = None, last_name: str = None,
        email_address: str = None, phone_number: str = None, hire_date: str = None, salary: float = None,
        department_id: int = None, hub_id: int = None, direct_reports: list = None):
        super().__init__(role_id, first_name, last_name, email_address, phone_number, hire_date, salary, department_id, hub_id)
        self.manager_id = manager_id



