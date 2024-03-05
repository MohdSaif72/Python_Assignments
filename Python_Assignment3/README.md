# Python Assignment 3

This is the python assignment which has questions related to decorators,Faker module and JSON files.

### Question 1 and 2
 Write a decorator to log the following details whenever a function is called

     a. The File needs to be name of the <module>_<YYYYMMDD>.log
	 b. The messages in the logs file should follow the format as below
		<module name> <function name> <DD-MM-YY> <hh:mm:ss> <Dict of Arguments passed to the function>
Write a decorator to log the execution time for a function. The time can be logged in the same file as above.

### Solution 1 and 2:
In this i defined a decorator function called 'log' that logs function calls,execution time, date, and arguments. The decorator captures the start and end times of function execution, calculates the duration, retrieves the current date and time, and logs this information along with the function's arguments into a file named after the module and date. 
### Question 3
Write a decorator to validate arguments passed to a function based on a condition.
e.g. Write a WAF to generate sequence of squares of all even numbers in the range of 1 to 10
Check if the number passed as a argument is in the specified range using decorators. If the condition fails the function 
should return an exception "ValueError" with an appropriate message.


### Solution 3:
In this i use a decorator validate to check if an input number is within the range of 1 to 10 before executing the 'even_squares' function, which calculates the squares of even numbers up to the given input. If the number is outside the range, a ValueError is raised. This code showcases how decorators can validate function inputs efficiently.

### Question 4
 Use the python Faker module to generate fake data for the following.
	a. Create an JSON File "Employee Personal Details" with following data. Generate around 50-100 records
		"EMP ID", "EMP NAME", "EMP EMAIL", "Businees Unit" "Salary".

### Solution 4:
In this i use the Faker library to create fake employee data, such as ID, name, email, business unit, and salary for a specified number of records. The 'generate_fake_data' function generates this data, while the 'json_file' function writes it to a JSON file. This code showcases how to efficiently generate data and store it in a structured format like JSON.

### Question 5
 Use the above created JSON File as an input to the following

	a. Create a JSON File to aggregate the above data w.r.t Businees Unit and store the Employee details. 
	
	b. Delete multiple employee and their corresponding details whenever an employee contract is 
	   terminated and maintain the name of the employee in a separate JSON file.
	   . Raise and exception whenever you are asked to delete the employee details that is not present.

	c. Fix a salary hike in terms of percentage for each Business Unit and update the salary figures
	for all employees based on the same.
### Solution 5:
In first part, i defined a function named 'aggregate' that reads employee data from a JSON file, aggregates it based on the business unit, and stores the aggregated details in a new JSON file. The function loads the input data, organizes it by business unit into a dictionary, and then writes this aggregated data to an output JSON file.

In second part, i defined a function 'delete_employees' that removes employees based on contract termination by their IDs from a JSON dataset. The function updates the data file, logs the terminated employees' names, and efficiently handles exceptions for missing employee IDs.

In third part, i defined a function 'salary_hike' that adjusts employee salaries based on predefined percentage hikes for different business units. The script reads employee data from a JSON file, applies the salary increases, and saves the updated information to a new JSON file.

### Modules Used:

- time
- json
- random
- faker
  
