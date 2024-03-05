"""
importing log function from decorators file
"""
from package.decorators import log

@log
def validate(func):
    """
    This function validates if the input number is within the range of 1 to 10.
    """
    def wrapper(num):
        if 1 <= num <= 10:
            return func(num)
        raise ValueError("Number is out of range")
    return wrapper

@validate
def even_squares(num):
    """
    This function calculates the squares of even numbers up to the given number.
    """
    return [x**2 for x in range(1, num+1) if x % 2 == 0]

try:
    result = even_squares(10)
    print(result)
except ValueError as e:
    print(e)
