import csv
from manager import Manager
from worker import Worker

CSV_FILE = 'employees.csv'
class filehandler:

    def save_employee(employee):
        with open(CSV_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            if isinstance(employee, Manager):
                writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), employee.get_department(), ''])
            elif isinstance(employee, Worker):
                writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), '', employee.get_hours_worked()])

    def load_employees():
        employees = []
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, age, salary, department, hours_worked = row
                if department:
                    employees.append(Manager(name, age, float(salary), department))
                else:
                    employees.append(Worker(name, age, float(salary), int(hours_worked)))
        return employees
    
    
    def update_employees(employees):
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            for employee in employees:
                if isinstance(employee, Manager):
                    writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), employee.get_department(), ''])
                elif isinstance(employee, Worker):
                    writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), '', employee.get_hours_worked()])


    def delete_employee(name):
        employees = filehandler.load_employees()
        employees = [emp for emp in employees if emp.get_name() != name]
        filehandler.update_employees(employees)