from fileEmployee import Employee
from server_mss import SqlQuery
from hrManagement import HrManagement
from fileHub import Hub


class Company:
    def __init__(self, ceo_name, cto_name, cfo_name):
        self.ceo_name = ceo_name
        self.cto_name = cto_name
        self.cfo_name = cfo_name
        self.db = SqlQuery()

    def add_hub(self, hub):
        query = f"INSERT INTO HUB (Hub_id, hub_manager_id, address_id, city, country) VALUES ({hub.hub_id}, {hub.hub_manager_id}, '{hub.address_id}', '{hub.city}', '{hub.country}')"
        self.db.query_set(query)












