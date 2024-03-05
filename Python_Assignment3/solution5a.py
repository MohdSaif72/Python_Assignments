"""
The json module in Python provides functions for encoding and decoding JSON data
"""
import json
from package.decorators import log

@log
def aggregate(input_file, output_file):
    """
    Aggregate employee data by Business Unit and store the details in a new JSON file.
    """
    with open(input_file, "r", encoding='utf-8') as file:
        data = json.load(file)
    aggregated_data = {}
    for record in data:
        business_unit = record["Business Unit"]
        if business_unit not in aggregated_data:
            aggregated_data[business_unit] = []
        aggregated_data[business_unit].append(record)

    with open(output_file, "w", encoding='utf-8') as file:
        json.dump(aggregated_data, file, indent=4)

    return aggregated_data

aggregate("Employee_Personal_Details.json", "Aggregated_Details.json")
