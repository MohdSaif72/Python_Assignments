"""
Counter is a sub-class that is used to count hashable objects.
"""
from collections import Counter
from package import decorators

def sort(item):
    """
    this function sorts elements
    """
    # Sort by occurrence count (descending)
    count = -item[1]
    # If occurrence count is the same, sort alphabetically
    char = item[0]
    return (count, char)

@decorators.log
def occurence(input_str):
    """
    this function gives the count of top three characters
    """
    # Count occurrences of each character
    char_count = Counter(input_str)
    # Get the top 3 characters based on  sorting criteria
    top_3 = sorted(char_count.items(), key=sort)[:3]
    # Print the top 3 characters along with their occurrence count
    for char, count in top_3:
        print(f"{char}: {count}")


#string = input("Enter the string: ")
STRING="HAPPIESTMINDS"
occurence(STRING)
