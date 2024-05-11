import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_inner_function(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        time.sleep(1)
        end_time = time.perf_counter()

        time_taken = end_time - start_time
        print(f"The {func.__name__} took {time_taken:.4f} seconds to run ....")
        return value
    
    return wrapper_inner_function

@timer
def add_first_and_last_name(firstName, lastName):
    return f"{firstName} {lastName}"

returned_value = add_first_and_last_name('Aman', 'Gaur')
print(returned_value)