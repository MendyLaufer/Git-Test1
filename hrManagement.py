from server_mss import SqlQuery


class HrManagement:

    def __init__(self):
        self.db = SqlQuery()


    def add_manager(self, manager):
        try:
            query = f"INSERT INTO MANGER (employee_id, role_id, first_name, last_name, email_address," \
                    f" phone_number, hire_date, salary ,department_id, hub_id) " \
                    f"VALUES ({manager.employee_id}, {manager.role_id}, '{manager.first_name}', '{manager.last_name}'," \
                    f"'{manager.email_address}', '{manager.phone_number}', '{manager.hire_date}', {manager.salary}," \
                    f" {manager.department_id}, {manager.hub_id})"
            self.db.query_set(query)
            print("Manager added successfully.")

        except AttributeError:
            print("Invalid manager or hub. Please provide existing manager and hub in the database.")

    def get_employee(self, employee_id):
        query = f"SELECT * FROM employee WHERE employee_id = {employee_id}"
        self.db.query_select(query)

    def add_employee(self, employee):
        try:
            query_manager = f"SELECT * FROM employee WHERE employee_id = {employee.manager.employee_id}"
            self.db.cursor1.execute(query_manager)
            manager_row = self.db.cursor1.fetchone()

            query_hub = f"SELECT * FROM Hub WHERE hub_id = {employee.branch.hub_id}"
            self.db.cursor1.execute(query_hub)
            branch_row = self.db.cursor1.fetchone()

            if manager_row and branch_row:
                query = f"INSERT INTO employee (employee_id, role_id, first_name, last_name, email_address," \
                        f" phone_number, hire_date, salary ,department_id, hub_id) " \
                        f"VALUES ({employee.employee_id}, {employee.role_id}, '{employee.first_name}', '{employee.last_name}'," \
                        f"'{employee.email_address}', '{employee.phone_number}', '{employee.hire_date}', {employee.salary}," \
                        f" {employee.department_id}, {employee.hub_id})"
                self.db.query_set(query)
                print("Employee added successfully.")
            else:
                print("Invalid manager or hub. Please provide existing manager and hub in the database.")

        except AttributeError:
            print("Invalid manager or hub. Please provide existing manager and hub in the database.")

    def delete_employee(self, employee_id):
        query = f"DELETE FROM employee WHERE employee_id = {employee_id}"
        self.db.query_set(query)

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

    def general_employees_sum(self):
        query = "SELECT SUM (salary) FROM employee"
        self.db.query_select(query)

    def add_hub(self, hub):
        query = f"INSERT INTO HUB (Hub_id, hub_manager_id, address_id, city, country) VALUES ({hub.hub_id}, {hub.hub_manager_id}, '{hub.address_id}', '{hub.city}', '{hub.country}')"
        self.db.query_set(query)






