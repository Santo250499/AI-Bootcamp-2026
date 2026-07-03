employees = [
    {
        "name": "John",
        "department": "ICT",
        "device": "Laptop"
    },
    {
        "name": "Sarah",
        "department": "HR",
        "device": "iPhone"
    },
    {
        "name": "Michael",
        "department": "Finance",
        "device": "Surface Pro"
    }
]


def view_employees():
    print("\n======== Employee List ========")

    if len(employees) == 0:
        print("No employees found.")
        return

    for index, employee in enumerate(employees, start=1):
        print(f"\n{index}. {employee['name']}")
        print(f"Department: {employee['department']}")
        print(f"Device: {employee['device']}")


def add_employee():
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    device = input("Enter device type: ")

    employee = {
        "name": name,
        "department": department,
        "device": device
    }

    employees.append(employee)
    print(f"\n{name} has been added successfully.")


def search_employee():
    search_name = input("Enter employee name to search: ")

    found = False

    for employee in employees:
        if employee["name"].lower() == search_name.lower():
            print("\nEmployee found:")
            print(f"Name: {employee['name']}")
            print(f"Department: {employee['department']}")
            print(f"Device: {employee['device']}")
            found = True
            break

    if not found:
        print("\nEmployee not found.")


def main():
    while True:
        print("\n======== Employee Management System ========")
        print("1. Add Employee")
        print("2. Search Employee")
        print("3. View Employees")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            search_employee()
        elif choice == "3":
            view_employees()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


main()