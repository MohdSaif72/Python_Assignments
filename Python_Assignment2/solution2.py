"""
Tabulate helps in creating and formatting the tables
"""
from tabulate import tabulate
import solution1b
from package import decorators

@decorators.log
def create_table():
    """
    This function will create formatted table displaying information about days of the week
    """
    tabledata = []
    for day, info in solution1b.dict_days().items():
        tabledata.append([day, info[0], info[1], info[2], info[3], info[4]])

    tableheaders = ["Name of the Day",
                     "Occurrences", 
                     "Short Form", 
                     "Name in Lower", 
                     "Name in Upper", 
                     "Length"]
    table = tabulate(tabledata, headers=tableheaders, tablefmt='grid')
    return table

# Call the user-defined function to create and display the table
print(create_table())