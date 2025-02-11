def my_decorator(input_func):
    def wrapper(*args, **kwargs):
        print('I use decorator')
        input_func(*args, **kwargs)

    return wrapper

@my_decorator
def sum_two_numbers(x,y):
    print(x + y)

sum_two_numbers(4,5)

