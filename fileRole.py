from server_mss import SqlQuery

class Role:
    def __init__(self, role_id, role_name=None, max_salary=None, min_salary=None):
        self.role_id = role_id
        self.role_name = role_name
        self.max_salary = max_salary
        self.min_salary = min_salary
        self.db = SqlQuery()

        query = f"INSERT INTO role (role_id, role_name, max_salary, min_salary) " \
                f"VALUES ({self.role_id}, '{self.role_name}', {self.max_salary}, {self.min_salary})"
        self.db.query_set(query)

    def print_sum_employee_role(self, role_id):
        query = f"SELECT count (*) FROM employee WHERE role_id = {role_id}"
        self.db.query_select(query)

    def insert_to_database(self):
        query = f"INSERT INTO role (role_id, role_name, max_salary, min_salary) " \
                f"VALUES ({self.role_id}, '{self.role_name}', {self.max_salary}, {self.min_salary})"
        self.db.query_set(query)

    def set_max_salary(self, role_id, max_salary):
        self.max_salary = max_salary
        self.role_id = role_id
        query = f"UPDATE role SET max_salary = {max_salary} WHERE role_id = {self.role_id}"
        self.db.query_set(query)

    def set_min_salary(self, role_id, min_salary):
        self.min_salary = min_salary
        self.role_id = role_id
        query = f"UPDATE role SET min_salary = {min_salary} WHERE role_id = {self.role_id}"
        self.db.query_set(query)

    def update_salary(self, role_id, min_salary, max_salary):
        self.role_id = role_id
        self.set_min_salary(role_id, min_salary)
        self.set_max_salary(role_id, max_salary)
        print("Role salary details updated successfully.")

    def delete_from_database(self):
        query = f"DELETE FROM role WHERE role_id = {self.role_id}"
        self.db.query_set(query)
