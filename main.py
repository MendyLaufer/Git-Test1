from fileCompany import Company
from fileEmployee import Employee
from hrManagement import HrManagement



company = Company("CEO Name", "CTO Name", "CFO Name")
number = int(input("For Employees Management Access Press: 1 \nFor Budgets Management Access Press: 2 \nFor Hubs and Departments Management Access Press: 3\n> "))
if number == 1:
    choice = int(input("to add employee press 1:\n to delete employee press 2:\n to change employee's details press 3:\n> "))
    if choice == 1:
        # Get employee details from user input
        employee_id = int(input("Enter employee ID: "))
        role_id = int(input("Enter role ID: "))
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email_address = input("Enter email address: ")
        phone_number = input("Enter phone number: ")
        hire_date = input("Enter hire date (YYYY-MM-DD): ")
        salary = float(input("Enter salary: "))
        department_id = int(input("Enter department ID: "))
        hub_id = int(input("Enter hub ID: "))

        # Create Employee object
        employee = Employee(employee_id, role_id, first_name, last_name, email_address, phone_number, hire_date, salary,
                            department_id, hub_id)

        # Add employee to the company
        HrManagement.add_employee(employee)

        print("Employee added successfully.")

    elif choice == 2:
        # Get employee ID to delete
        employee_id = int(input("Enter employee ID to delete: "))

        # Delete employee from the company
        hr_manager = HrManagement()
        hr_manager.delete_employee(employee_id)

elif number == 2:
    pass
# employee = Employee(209,  1, "John", "Doe", "john@example.com", "123456789", "2023-06-27", 5000.0)
# employee.set_hub_id()


