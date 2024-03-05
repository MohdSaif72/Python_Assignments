# Python Assignment 1

This is the python assignment which has questions related to strings and running processes.

### Question 1 
Given a String of Characters
1. Print the three most common characters along with their occurrence count.
2. Sort in descending order of occurrence count.
3. If the occurrence count is the same for any character, sort the characters in alphabetical order.

Final Output. 

Top 3 Characters based on the above critera

E.g. 

Input: HAPPIESTMINDS

Output : 

I: 2

P: 2

S: 2

### Solution 1:
In this i imported the Counter class from the collections module and the log decorator from a custom log module. I define a sort function to sort elements based on their occurrence count and alphabetical order. The occurrence function, decorated with log, counts the occurrences of characters in a given input string, sorts them based on a criteria defined by the sort function, and then prints the top three characters along with their occurrence count. 

### Question 2
Write a Program 
1. to find all the list of all running process in your System
2. Display the count of each running process.
3. Store this information in a CSV File.

### Solution 2:
In this i used the csv and psutil modules, along with a custom log decorator, to retrieve information about running processes, count their occurrences, and save the data to a CSV file. It gathers process details, counts their occurrences, prints the results, and then writes this information to a CSV file named 'processes.csv'.

### Question 3
 Write a program to monitor the applications running on your system. 
To test: Execute any application like browser, notepad, calculator etc and make sure 
that not more than 2 instances of the same application can be running.
 

### Solution 3:
In this i defined two functions: 'count_instances' and 'monitor_applications'. The count_instances function uses the psutil library to count instances of a specified process name, terminating any excess instances beyond the defined maximum. The 'monitor_applications' function, decorated with a custom log decorator, checks the running instances of applications in a list, alerting if they exceed the maximum allowed, and displaying the current number of instances for each application.


### Question 4
Write a program to return below output from given input (with and without uses of inbuilt function)

Input -  "My name is Suraj"

output - "Suraj is name My"

### Solution 4:
In this i defined a function 'reverse' that takes a string input, splits it into words, reverses their order, and reconstructs the sentence. The first snippet uses the reversed function to reverse the words, while the second snippet manually iterates over the list indices to achieve the same result. Both snippets employ a custom log decorator from the decorators package to log function calls. The scripts prompt the user for a sentence, apply the reverse function to reverse the input, and output the reversed sentence.

### Question 5
Write a program to print fibonacci series for the given input occurence (if user gives i\p as 6 then it should print series till 6th number)
FiBoNACCI series
0 1 1 2 3 5 8 13 21
 
Input: 6, Output: 0 1 1 2 3 5

Input: 10, Output: 0 1 1 2 3 5 8 12 21 34
### Solution 5:
In this i defined a function 'fib' to generate the first n Fibonacci numbers. It initializes the sequence and iterates to calculate each Fibonacci number by adding the previous two. The script prompts the user for a number, generates the Fibonacci sequence, and prints it.


### Modules Used:

- collections
- csv
- psutil
  
