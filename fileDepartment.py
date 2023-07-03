from server_mss import SqlQuery
from fileRole import Role

class Department:
    def __init__(self, department_id=0, department_name=0, manager_id=0, hub_id=0):
        self.department_id = department_id
        self.department_name = department_name
        self.manager_id = manager_id
        self.hub_id = hub_id
        self.db = SqlQuery()

    def add_role(self, role_id, role_name, max_salary, min_salary):
        role = Role(role_id, role_name, max_salary, min_salary)
        role.insert_to_database()

    def remove_role(self, role_id):
        role = Role(role_id)
        role.delete_from_database()








