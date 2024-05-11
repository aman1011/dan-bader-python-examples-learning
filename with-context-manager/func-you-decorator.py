import functools

def do_thrice(func):
    @functools.wraps(func)
    def wrapper_inner_function(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_inner_function

@do_thrice
def say_whee_with_name(name):
    print(f"say whee to {name} ....")
    return f"say whee to {name} ...."

say_whee_with_name('slim shady')