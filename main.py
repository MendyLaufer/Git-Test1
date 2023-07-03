from fileCompany import Company
from fileEmployee import Employee
from hrManagement import HrManagement
from fileRole import Role
from fileHub import Hub


company = Company("CEO Name", "CTO Name", "CFO Name")
number = int(input("For Employees Management Access Press: 1 \nFor Budgets Management Access Press: 2 \n"
                   "For Hubs and Departments Management Access Press: 3\n> "))

while True:
    if number == 1:
        choice = int(input("to add employee press 1:\nto delete employee press 2:\nto change employee's details press 3:\n"
                           "to get employee's details press 4:> "))

        if choice == 1:
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

            employee = Employee(employee_id, role_id, first_name, last_name, email_address, phone_number, hire_date, salary,
                                department_id, hub_id)

            hr_manager = HrManagement()
            hr_manager.add_employee(employee)
            print("Employee added successfully.")

        elif choice == 2:
            employee_id = int(input("Enter employee ID to delete: "))

            hr_manager = HrManagement()
            hr_manager.delete_employee(employee_id)
            print("Employee deleted successfully.")

        elif choice == 3:
            employee_id = int(input("Enter employee ID: "))
            change_option = int(input("Choose the detail to change:\n1. Role ID\n2. Phone Number\n3. Salary\n4. "
                                      "Department ID\n5. Hub ID\n> "))

            # employee_id = int(input("Enter employee ID: "))
            employee = Employee(employee_id)
            # change_option = int(input("Enter the change option (1-5): "))
            if change_option == 1:
                role_id = int(input("Enter new role ID: "))
                employee.set_role_id(employee_id, role_id)
            elif change_option == 2:
                phone_number = input("Enter new phone number: ")
                employee.update_phone(employee_id, phone_number)
            elif change_option == 3:
                salary = float(input("Enter new salary: "))
                employee.set_salary(employee_id, salary)
            elif change_option == 4:
                department_id = int(input("Enter new department ID: "))
                employee.set_department_id(employee_id, department_id)
            elif change_option == 5:
                hub_id = int(input("Enter new hub ID: "))
                employee.set_hub_id(employee_id, hub_id)
            else:
                print("Invalid number. Please enter a number between 1 and 5.")
            print("Employee details updated successfully.")

        elif choice == 4:
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
            role = Role(role_id, "", 0, 0)
            role.print_sum_employee_role(role_id)

        else:
            print("Invalid number. Please enter a number between 1 and 2.")

    elif number == 3:
        choice1 = int(input("To add a new branch press 1:\nTo set hub manager id press 2:\n"
                            "To add a department press 3:\nTo remove a department press 4:\n"
                            "To update role's salary details press 5:\n"))

        if choice1 == 1:
            hub = Hub(
                hub_id=int(input("Enter new hub_id: ")),
                hub_manager_id=int(input("Enter new hub manager id: ")),
                address_id=int(input("Enter new address id: ")),
                city=input("Enter new city: "),
                country=input("Enter new country: ")
            )
            company.add_hub(hub)
            print("Hub added successfully.")

        elif choice1 == 2:
            manager_id = int(input("Enter manager ID: "))
            hub_id = int(input("Enter hub ID: "))
            hr_manager = HrManagement()
            hr_manager.set_hub_manager_id(manager_id, hub_id)
            print("Hub manager ID updated successfully.")

        elif choice1 == 3:
            department_id = int(input("Enter department ID: "))
            department_name = input("Enter department name: ")
            hr_manager = HrManagement()
            hr_manager.add_department(department_id, department_name)
            print("Department added successfully.")

        elif choice1 == 4:
            department_id = int(input("Enter department ID: "))
            hr_manager = HrManagement()
            hr_manager.remove_department(department_id)
            print("Department removed successfully.")

        elif choice1 == 5:
            role_id = int(input("Enter role ID: "))
            min_salary = float(input("Enter minimum salary: "))
            max_salary = float(input("Enter maximum salary: "))

            role = Role(role_id=role_id)
            role.update_salary(min_salary, max_salary)
            print("Role salary details updated successfully.")


        else:
            print("Invalid number. Please enter a number between 1 and 5.")

    else:
        print("Invalid number. Please enter a number between 1 and 3.")
