"""
Time module helps in time related tasks
"""
import time

def log(func):
    """
    This decorator function logs the function calls along with execution time, date, and arguments.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        current_date = time.strftime('%Y-%m-%d')
        current_time = time.strftime('%H:%M:%S')
        arguments = kwargs

        file_name = f"{func.__module__}{current_date}.log"
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f"{func.__module__} {func.__name__} \n")
            file.write(f"{current_date} {current_time} {arguments}\n")
            file.write(f"Execution time: {execution_time} seconds\n\n")

        return result
    return wrapper
