import re


class Employee:
    def __init__(self, employee_id, role_id, first_name, last_name, email_address, phone_number, hire_date, salary,
                 department_id, hub_id):
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


class HrManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def delete_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                break

    def set_role_id(self, employee_id, role_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.role_id = role_id
                break

    def update_phone(self, employee_id, phone_number):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.phone_number = phone_number
                break

    def set_salary(self, employee_id, salary):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.salary = salary
                break

    def set_department_id(self, employee_id, department_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.department_id = department_id
                break

    def set_hub_id(self, employee_id, hub_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.hub_id = hub_id
                break


def display_menu():
    print("Welcome to the HR Management System!")
    print("===================================")
    print("1. Employees Management")
    print("2. Budgets Management")
    print("3. Hubs and Departments Management")


def display_employee_menu():
    print("Employees Management")
    print("====================")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Change Employee's Details")


def validate_phone_number(phone_number):
    pattern = r'^\d{8,13}$'
    return re.match(pattern, phone_number) is not None


def validate_email_address(email_address):
    pattern = r'^[\w.-]+@[a-zA-Z]+\.[a-zA-Z]{2,3}$'
    return re.match(pattern, email_address) is not None


def validate_name(name):
    pattern = r'^[a-zA-Z ]+$'
    return re.match(pattern, name) is not None


def validate_date(date):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return re.match(pattern, date) is not None


def add_employee(hr_manager):
    employee_id = int(input("Enter employee ID: "))
    role_id = int(input("Enter role ID: "))
    first_name = input("Enter first name: ")
    while not validate_name(first_name):
        print("Invalid name. Please enter letters only.")
        first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    while not validate_name(last_name):
        print("Invalid name. Please enter letters only.")
        last_name = input("Enter last name: ")
    email_address = input("Enter email address: ")
    while not validate_email_address(email_address):
        print("Invalid email address format. Please enter a valid email address.")
        email_address = input("Enter email address: ")
    phone_number = input("Enter phone number: ")
    while not validate_phone_number(phone_number):
        print("Invalid phone number. Please enter a number with 8 to 13 digits.")
        phone_number = input("Enter phone number: ")
    hire_date = input("Enter hire date (YYYY-MM-DD): ")
    while not validate_date(hire_date):
        print("Invalid date format. Please enter in the format YYYY-MM-DD.")
        hire_date = input("Enter hire date (YYYY-MM-DD): ")
    salary = float(input("Enter salary: "))
    department_id = int(input("Enter department ID: "))
    hub_id = int(input("Enter hub ID: "))

    employee = Employee(
        employee_id, role_id, first_name, last_name, email_address, phone_number, hire_date, salary, department_id,
        hub_id
    )

    hr_manager.add_employee(employee)

    print("Employee added successfully.")


def delete_employee(hr_manager):
    employee_id = int(input("Enter employee ID to delete: "))
    hr_manager.delete_employee(employee_id)
    print("Employee deleted successfully.")


def change_employee_details(hr_manager):
    employee_id = int(input("Enter employee ID: "))
    change_option = int(input(
        "Choose the detail to change:\n1. Role ID\n2. Phone Number\n3. Salary\n4. Department ID\n5. Hub ID\n> "))

    if change_option == 1:
        role_id = int(input("Enter new role ID: "))
        hr_manager.set_role_id(employee_id, role_id)
    elif change_option == 2:
        phone_number = input("Enter new phone number: ")
        while not validate_phone_number(phone_number):
            print("Invalid phone number. Please enter a number with 8 to 13 digits.")
            phone_number = input("Enter new phone number: ")
        hr_manager.update_phone(employee_id, phone_number)
    elif change_option == 3:
        salary = float(input("Enter new salary: "))
        hr_manager.set_salary(employee_id, salary)
    elif change_option == 4:
        department_id = int(input("Enter new department ID: "))
        hr_manager.set_department_id(employee_id, department_id)
    elif change_option == 5:
        hub_id = int(input("Enter new hub ID: "))
        hr_manager.set_hub_id(employee_id, hub_id)
    else:
        print("Invalid option.")

    print("Employee details updated successfully.")


# Main program
def main():
    hr_manager = HrManagement()

    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_employee_menu()
        emp_choice = int(input("Enter your choice: "))

        if emp_choice == 1:
            add_employee(hr_manager)
        elif emp_choice == 2:
            delete_employee(hr_manager)
        elif emp_choice == 3:
            change_employee_details(hr_manager)
        else:
            print("Invalid choice.")
    elif choice == 2:
        # Budgets Management
        pass
    elif choice == 3:
        # Hubs and Departments Management
        pass
    else:
        print("Invalid choice.")

    print("Thank you for using the HR Management System!")


if __name__ == "__main__":
    main()
