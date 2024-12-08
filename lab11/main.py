from manager import Manager
from worker import Worker
from Filehandiling import filehandler


def add_employee():
    emp_type = input("Enter employee type (Manager/Worker): ").strip().lower()
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))

    if emp_type == 'manager':
        department = input("Enter department: ")
        emp = Manager(name, age, salary, department)
    elif emp_type == 'worker':
        hours_worked = int(input("Enter hours worked: "))
        emp = Worker(name, age, salary, hours_worked)
    else:
        print("Invalid employee type!")
        return
    
    filehandler.save_employee(emp)
    print(f"{emp_type.capitalize()} added successfully!")

def display_employees():
    employees = filehandler.load_employees()
    for emp in employees:
        if isinstance(emp, Manager):
            print(f"Manager - Name: {emp.get_name()}, Age: {emp.get_age()}, Salary: {emp.get_salary()}, Department: {emp.get_department()}")
        elif isinstance(emp, Worker):
            print(f"Worker - Name: {emp.get_name()}, Age: {emp.get_age()}, Salary: {emp.get_salary()}, Hours Worked: {emp.get_hours_worked()}")

def update_employee():
    name = input("Enter the name of the employee to update: ")
    employees = filehandler.load_employees()
    for emp in employees:
        if emp.get_name() == name:
            age = int(input("Enter new age: "))
            salary = float(input("Enter new salary: "))
            emp.set_age(age)
            emp.set_salary(salary)
            if isinstance(emp, Manager):
                department = input("Enter new department: ")
                emp.set_department(department)
            elif isinstance(emp, Worker):
                hours_worked = int(input("Enter new hours worked: "))
                emp.set_hours_worked(hours_worked)
            filehandler.update_employees(employees)
            print("Employee information updated successfully!")
            return
    print("Employee not found!")

def delete_employee():
    name = input("Enter the name of the employee to delete: ")
    filehandler.delete_employee(name)
    print("Employee deleted successfully!")

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")
main()
