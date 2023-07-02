from server_mss import SqlQuery


class Role:
    def __init__(self, role_id, role_name, max_salary, min_salary):
        self.role_id = role_id
        self.role_name = role_name
        self.max_salary = max_salary
        self.min_salary = min_salary
        self.db = SqlQuery()

        query = f"INSERT INTO role (role_id, role_name, max_salary, min_salary) " \
                f"VALUES ({self.role_id}, '{self.role_name}', {self.max_salary}, {self.min_salary})"
        self.db.query_set(query)

    def set_max_salary(self, max_salary):
        self.max_salary = max_salary
        query = f"UPDATE role SET max_salary = {max_salary} WHERE role_id = {self.role_id}"
        self.db.query_set(query)

    def set_min_salary(self, min_salary):
        self.min_salary = min_salary
        query = f"UPDATE role SET min_salary = {min_salary} WHERE role_id = {self.role_id}"
        self.db.query_set(query)

    def print_sum_employee_role(self, role_id):
        query = f"SELECT count (*) FROM employee WHERE role_id = {role_id}"
        self.db.query_select(query)

