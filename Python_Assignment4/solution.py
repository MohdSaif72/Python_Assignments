""" 
The json module in Python provides functions for encoding and decoding JSON data
"""
import json
import os
from faker import Faker
from package import decorators

fake = Faker()

class Employee:
    """
    This class represents an employee with attributes ID, name, email, business unit, and salary.
    """
    def __init__(self, emp_id=None, emp_name=None, emp_email=None, business_unit=None, salary=None):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_email = emp_email
        self.business_unit = business_unit
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.emp_name},Email: {self.emp_email},Business Unit: {self.business_unit}, Salary: {self.salary}"

    # Getter methods
    def get_id(self):
        """ getter method for emp id """
        return self.emp_id

    def get_name(self):
        """ getter method for emp name """
        return self.emp_name

    def get_email(self):
        """ getter method for emp email """
        return self.emp_email

    def get_business_unit(self):
        """ getter method for business unit """
        return self.business_unit

    def get_salary(self):
        """ getter method for salary """
        return self.salary

    # Setter methods
    def set_id(self, emp_id):
        """ setter method for emp id """
        self.emp_id = emp_id

    def set_name(self, emp_name):
        """ setter method for emp name"""
        self.emp_name = emp_name

    def set_email(self, emp_email):
        """ setter method for emp email"""
        self.emp_email = emp_email

    def set_business_unit(self, business_unit):
        """ setter method for business unit"""
        self.business_unit = business_unit

    def set_salary(self, salary):
        """ setter method for salary"""
        self.salary = salary

    # Setter methods with Faker defaults
    def set_name_default(self):
        """ setter method for emp id """
        self.emp_name = fake.name()

    def set_email_default(self):
        """ setter method for emp email """
        self.emp_email = fake.email()

    def set_business_unit_default(self):
        """ setter method for business unit"""
        self.business_unit = fake.random.choice(["Sales", "Marketing", "IT"])

    def set_salary_default(self):
        """ setter method for salary"""
        self.salary = fake.random_int(min=30000, max=150000)

    def write_to_file(self,employee_data, file_name='employees.json'):
        """ Writes data to a JSON file with specified formatting """
        with open(file_name, 'w',encoding='utf-8') as json_file:
            json.dump(employee_data, json_file, indent=4)

    def json(self):
        """ Converts employee data to a JSON-compatible dictionary format """
        return {
            "EMP ID": self.emp_id,
            "EMP NAME": self.emp_name,
            "EMP EMAIL": self.emp_email,
            "Business Unit": self.business_unit,
            "Salary": self.salary
        }
  
    def one_data_file(self, file_name='employees.json'):
        """  Writes data of a single employee to a JSON file """
        employee_data = self.json()
        Employee.write_to_file(employee_data, file_name)
    
    @classmethod
    def all_data_file(cls, employees, file_name='employees.json'):
        """ Writes data of multiple employees to a JSON file """
        employee_data = [emp.json() for emp in employees]
        cls.write_to_file(employee_data, file_name)

@decorators.log
def employee_records(directory, file):
    """
    This method loads employee data from a JSON file specified by the directory and filename.
    """
    file_path = os.path.join(directory, file)

    if os.path.exists(file_path):
        employees = []
        with open(file_path, "r", encoding="utf-8") as jsonfile:
            loaded_data = json.load(jsonfile)
            for record in loaded_data:
                records = Employee(record.get("EMP ID"), record.get("EMP NAME"), record.get("EMP EMAIL"), record.get("Business Unit"), record.get("Salary"))
                employees.append(records)
        return employees

DIRECTORY = "C:\\Users\\mohd.ali\\OneDrive - Happiest Minds Technologies Limited\\Desktop\\Python Assignments\\Python_Assignment3"
FILE = "Employee_Personal_Details.json"

data = employee_records(DIRECTORY, FILE)

for employee in data[:1]:
    print(employee)

employee1 = data[0]
print("Name:", employee1.get_name())

employee1.set_name("Saif")
print("Name:", employee1.get_name())

employee1.set_name_default()
print("Name:", employee1.get_name())

employee1.one_data_file("One_employee.json")

# For a list of employees
Employee.all_data_file(data[:1], "list_employees.json")

# For all employees (by default)
Employee.all_data_file(data)
