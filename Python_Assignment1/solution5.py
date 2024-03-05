"""
importing wrapper function from decorators
"""
from package import decorators
@decorators.log
def fib(number):
    """
    function to return series of fibonacci
    """
    #inititialize the series with 0,1
    series = [0, 1]
    if number <= 1:
        return series[:number]
    #Iterate until length of series becomes equal to n
    while len(series) < number:
        #calculating the next Fibonacci number
        next_int= series[-1] + series[-2]
        #appending next number to the series
        series.append(next_int)
    return series

n = int(input("Enter the number: "))
fibonacci = fib(n)
print(*fibonacci)