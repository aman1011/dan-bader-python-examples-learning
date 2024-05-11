def do_twice(func):
    def wrapper_inner_function():
        func()
        func()

    return wrapper_inner_function


@do_twice
def say_whee():
    print("Say whee")

say_whee()
