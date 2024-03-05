"""
The json module in Python provides functions for encoding and decoding JSON data
"""
import json
import random
from faker import Faker
from package.decorators import log

fake = Faker()

@log
def generate_fake_data(records):
    """
    Generates fake employee data based on the specified number of records.
    """
    data = []
    for _ in range(records):
        emp_id = fake.random_int(min=1000, max=9999)
        emp_name = fake.name()
        emp_email = fake.email()
        business_unit = random.choice(["Cars and Co.", "Steel Ltd.", "IT"])
        salary = fake.random_int(min=30000, max=100000)

        data.append({
            "EMP ID": emp_id,
            "EMP NAME": emp_name,
            "EMP EMAIL": emp_email,
            "Business Unit": business_unit,
            "Salary": salary
        })
    return data

def json_file(data, filename):
    """
    Writes the provided data to a JSON file with the specified filename.
    """
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)

employee_data = generate_fake_data(55)
json_file(employee_data, "Employee_Personal_Details.json")
