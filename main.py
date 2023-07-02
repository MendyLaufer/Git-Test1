from fileCompany import Company
from fileEmployee import Employee
from hrManagement import HrManagement
from fileManager import Manager




company = Company("CEO Name", "CTO Name", "CFO Name")
number = int(input("For Employees Management Access Press: 1 \nFor Budgets Management Access Press: 2 \n"
                   "For Hubs and Departments Management Access Press: 3\n> "))
while True:
    if number == 1:
        choice = int(input("to add employee press 1:\nto delete employee press 2:\nto change employee's details press 3:\n"
                           "to get employee's details press 4:> "))
        if choice == 1:
            # Get employee details from user input
            employee_id = input("Enter employee ID: ")
            role_id = input("Enter role ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email_address = input("Enter email address: ")
            phone_number = input("Enter phone number: ")
            hire_date = input("Enter hire date (YYYY-MM-DD): ")
            salary = input("Enter salary: ")
            department_id = input("Enter department ID: ")
            hub_id = input("Enter hub ID: ")

            # Create Employee object
            employee = Employee(employee_id, role_id, first_name, last_name, email_address, phone_number, hire_date, salary,
                                department_id, hub_id)

            # Add employee to the company
            hr_manager = HrManagement()
            hr_manager.add_employee(employee)
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
            change_option = int(input("Choose the detail to change:\n1. Role ID\n2. Phone Number\n3. Salary\n4. "
                                      "Department ID\n5. Hub ID\n> "))

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
                print("Invalid number. Please enter a number between 1 and 5.")
            print("Employee details updated successfully.")
        if number == 4:
            employee_id = int(input("Enter employee ID: "))
            hr_manager = HrManagement()
            hr_manager.get_employee(employee_id)
        else:
            print("Invalid number. Please enter a number between 1 and 4.")
    elif number == 2:
        choice = int(input("to print general employees sum press 1:\n to print the sum of employee in role press 2:\n"))
        if choice == 1:
            hr_manager = HrManagement()
            hr_manager.general_employees_sum()
        elif choice == 2:
            role_id = int(input("Enter role ID: "))
            role = Role()
            role.print_sum_employee_role(role_id)
    elif number == 3:
        choice1 = int(input("To add a new branch press 1:\nTo set hub manager id press 2:"))
        if choice1 == 1:
            hub = Hub(
                hub_id=int(input("Enter new hub_id:")),
                hub_manager_id=int(input("Enter new hub manager id:")),
                address_id=int(input("Enter new address id:")),
                city=input("Enter new city:"),
                country=input("Enter new country:")
            )
            hr = HrManagement()
            hr.add_hub(hub)
        elif choice1 == 2:
            manager = int(input("Please enter manager id:"))

    else:
        print("Invalid number. Please enter a number between 1 and 3.")





