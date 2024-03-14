## Description
This Python script provides a basic Employee Data. It allows you to define an Employee class, set and get employee attributes, and convert employee data to JSON format and store it in a file.

## Problem Statement

Use the python Faker module to generate fake data for the following.
a. Create an JSON File "Employee Personal Details" with following data. Generate around 50-100 records
	"EMP ID", "EMP NAME", "EMP EMAIL", "Businees Unit" "Salary"
Note: This is already done as a part of the last assignment.

User the above as input data and do the following.

1. Define a class for the Employee and load all the data as Objects of this class.

2. Define setter methods for every attribute of the class.
    a. Set the value passed to it as a parameter
    b. Use Faker module to set the value as default

3. Define getter methods for very attribute of the class.

4. Define a method in the class to convert the Employee object to a JSON and write it to a file.
    The function should be able to do it for 
    * one employee
    * List of Employees 
    * All(by default)

## Features
- Define an Employee class with attributes such as ID, name, email, business unit, and salary.
  __init__(self, emp_id, emp_name, emp_email, business_unit, salary)
- Setter and getter methods for each attribute.
- Utilize the Faker module to generate default values for attributes.
- Convert employee data to JSON format.
  json(self): Converts the employee object to a JSON object.
- Write employee data to JSON files.
- Load employee data from JSON files.

## Requirements
- Python 3.x
- Faker module (pip install faker)

## File Structure
Employee.py: Contains the Employee class and its methods.

decorators.py: Contains decorator functions for logging.

Employee_Personal_Details.json: Sample JSON file containing employee data.

## Modules Required
- import json
- import os
- from package import decorators

