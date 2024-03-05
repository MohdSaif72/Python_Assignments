# Python Assignment 2

This is the python assignment which has questions related to tuple, list and dictionaries.

### Question 1
Create a Tuple with all Days of the week starting from Monday and output the following 

a. A list of tuples which has the two consequtive days grouped together

b. A dictionary which has the name of the day as the key and value as a tuple with following values

    i. Occurence of the day in a week (e.g. 1 for Monday, 2 for Tuesday)
    ii. Short form of the day (first three letters)
    iii. name of the day in the lower case
    iv. name of the day in the upper case
	v. length of each name
c. A tuple with all the characters and their number of occurences in each name of the day.

### Solution 1:
For first part i created a function grouped_days() that constructs a list of tuples representing consecutive pairs of days of the week. It iterates through the days from Monday to Sunday, creating tuples of consecutive days and storing them in a list. The function then returns this list of paired days.

For second part i created a dict_days() function generates a dictionary where each day of the week is a key, and the corresponding value is a tuple containing the day's occurrence in a week, its short form (first three letters), name in lowercase, name in uppercase, and the length of the day's name. This function gives the dictionary format.

For third part i created a occur_char() function generates a tuple containing the characters present in each day name and their respective counts. It uses the collections.Counter() method to count the occurrences of each character in the day name, and then stores the results in a tuple. 
### Question 2
Using the Dictionary output from assignment 1.b print the output as a Table. The Headers of a Table are as follows
"Name of the Day", "Occurences", Short Form", "Name in Lower", "Name in upper", "Length"

### Solution 2:
In this i have used tabulate library to create a formatted table displaying information about each day of the week. It retrieves data from the dict_days() function, organizes it into a list, and then uses tabulate to generate a grid-style table with headers for the name of the day, occurrences, short form, name in lowercase, name in uppercase, and length.

### Question 3
Write the output table from assignment 2 into an Excel File (not CSV).

### Solution 3:
In this i have used Pandas to convert the returned lists from solution1a, solution1b, and solution1c into DataFrames. Then, exports these DataFrames into separate Excel files with specified filenames.

### Question 4
Use the python Faker module to generate fake data for the following.

a. Create an excel sheet "Employee Personal Details" with following data. Generate around 50-100 records
		"EMP ID", "EMP NAME", "EMP EMAIL", "Businees Unit" "Salary"

	4a. WAF to return the empolyee name with top most salary
	4b. WAF to return the Business Unit with top most aggregated salary
	4c. WAF to return the employee name in each Business Unit with top most salary
	4d. WAF Delete the Record of the Employee name from the Excel File with the least salary.
	4e. WAF to Update the Salary Details of an Employee in the Excel File

### Solution 4:
In this i generated the fake employee data, writes it to an Excel file, reads the data back from the Excel file, calculates the top salary employee, top aggregated salary business unit, top salary employee in each business unit, removes the record of the employee with the least salary, updates the salary details of an employee, and outputs the updated data. It utilizes openpyxl to work with Excel files.


### Modules Used:

- collections
- tabulate
- pandas
- openpyxl
- random
- faker
