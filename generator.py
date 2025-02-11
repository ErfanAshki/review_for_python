def outer_decorator(n):
    def run_many_times(input_func):
        def wrapper():
            for i in range(n):
                input_func()
        return wrapper
    return run_many_times


@outer_decorator(4)
def first_name():
    print('Erfan')

@outer_decorator(2)
def last_name():
    print('Ashki')

first_name()
last_name()

