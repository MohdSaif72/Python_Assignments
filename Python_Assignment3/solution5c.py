"""
The json module in Python provides functions for encoding and decoding JSON data
"""
import json
from package.decorators import log

@log
def salary_hike(input_file):
    """
    Apply salary hike based on business unit percentages to employee data.
    """
    hike_percentages = {
        "Cars and Co.": 10,
        "Steel Ltd.": 12,
        "IT": 14
    }

    with open(input_file, 'r', encoding='utf-8') as file:
        employee_data = json.load(file)

    for employee in employee_data:
        business_unit = employee['Business Unit']
        if business_unit in hike_percentages:
            hike_percent = hike_percentages[business_unit]
            salary = employee['Salary']
            new_salary = salary * (1 + hike_percent / 100)
            employee['Salary'] = round(new_salary, 2)

    return employee_data

EMPLOYEE_FILE = "Updated_Employee_Personal_Details.json"
updated_employee_data = salary_hike(EMPLOYEE_FILE)

OUTPUT_FILE = "Hiked_Salary.json"
with open(OUTPUT_FILE, 'w', encoding='utf-8') as file_out:
    json.dump(updated_employee_data, file_out, indent=4)
