import sys

# Open the file in write mode
with open('output.txt', 'w') as f:
    # Write the console output to the file
    f.write(sys.stdout.getvalue())

# Print a message to the console
print('Console output written to output.txt')