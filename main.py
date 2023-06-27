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
        print("Employee deleted successfully.")

    elif choice == 3:
        employee_id = int(input("Enter employee ID: "))
        change_option = int(input(
            "Choose the detail to change:\n1. Role ID\n2. Phone Number\n3. Salary\n4. Department ID\n5. Hub ID\n> "))

        hr_manager = HrManagement()

        if change_option == 1:
            role_id = int(input("Enter new role ID: "))
            hr_manager.set_role_id(employee_id, role_id)
        elif change_option == 2:
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


elif number == 2:
    pass
# employee = Employee(209,  1, "John", "Doe", "john@example.com", "123456789", "2023-06-27", 5000.0)
# employee.set_hub_id()


