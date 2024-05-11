def do_twice(func):
    def wrapper_inner_func(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_inner_func


@do_twice
def say_name(name):
    print(f"my name is {name} ....")


say_name('slim_shady')