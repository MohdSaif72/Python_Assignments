"""
The json module in Python provides functions for encoding and decoding JSON data
"""
import json
from package.decorators import log

@log
def delete_employees(employee_ids, input_file, output_file, filename):
    """
    Delete multiple employees based on contract termination.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    terminated_employees = []
    for employee_id in employee_ids:
        terminated_employee = None
        for employee in data[:]:
            if employee["EMP ID"] == employee_id:
                terminated_employee = employee
                data.remove(employee)
                terminated_employees.append(terminated_employee)
                break

        if terminated_employee is None:
            raise ValueError(f"Employee with ID {employee_id} not found.")

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    with open(filename, 'a', encoding='utf-8') as file:
        for terminated_employee in terminated_employees:
            json.dump({"EMP NAME": terminated_employee["EMP NAME"]}, file)
            file.write('\n')

    return data

updated_data = delete_employees([5803,8002],
                                'Employee_Personal_Details.json', 
                                'Updated_Employee_Personal_Details.json', 
                                'Terminated_Employee_Names.json')
