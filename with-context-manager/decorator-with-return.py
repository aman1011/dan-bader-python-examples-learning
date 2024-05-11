def do_twice(func):
    def wrapper_inside_function(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    
    return wrapper_inside_function

@do_twice
def say_whee(name):
    print(f"my name is {name} ....")
    return f"my name is {name} ...."


returned_value = say_whee('slim_shady')
print(returned_value)