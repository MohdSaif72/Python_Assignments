"""
The csv module implements classes to read and write tabular data in CSV format.
"""
import csv
import psutil
from package import decorators

def run_proc():
    """
    this function gives the list of running processes
    """
    processes = []
    # Iterate over all running processes
    for proc in psutil.process_iter():
        # Get process information such as process ID and name
        process_info = proc.as_dict(attrs=['pid', 'name'])
        # Append process information to the list
        processes.append(process_info)
    return processes

# Function to count the occurrences of each process
def count_processes(processes):
    """
    this function gives the count of running processes
    """
    process_count_data = {}
    # Iterate over each process
    for process in processes:
        # Extract the process name
        process_data = process['name']
        # Update the count for the process name
        process_count_data[process_data] = process_count_data.get(process_data, 0) + 1
    return process_count_data

# Function to save process information to a CSV file
@decorators.log
def save_to_csv(process_count_data):
    """
    this function writes into csv file
    """
    with open('processes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Process Name', 'Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for name, count_val in process_count_data.items():
            writer.writerow({'Process Name': name, 'Count': count_val})
    print("Process information saved to 'processes.csv'")

# Retrieve information about running processes
running_processes = run_proc()

# Count occurrences of each process
process_count = count_processes(running_processes)

# Print process names and their counts
for process_name, count in process_count.items():
    print(f"{process_name}: {count}")

# Save process information to a CSV file
save_to_csv(process_count)
