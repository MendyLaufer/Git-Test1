from server_mss import SqlQuery

class Hub:
    def __init__(self, hub_id, hub_manager_id, address_id, city, country):
        self.hub_id = hub_id
        self.hub_manager_id = hub_manager_id
        self.address_id = address_id
        self.city = city
        self.country = country
        self.db = SqlQuery()

    def set_hub_manager_id(self, manager_id):
        query = f"UPDATE Hub SET hub_manager_id = {manager_id} WHERE hub_id = {self.hub_id}"
        self.db.query_set(query)

    def hub_employees_sum(self):
        query = f"SELECT COUNT(*)  FROM Employee WHERE hub_id = {self.hub_id}"
        self.db.query_select(query)

    def hub_salary_sum(self):
        query = f"SELECT SUM(salary) FROM Employee WHERE hub_id = {self.hub_id}"
        self.db.query_select(query)

