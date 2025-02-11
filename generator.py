def run_twice(input_func):
    def wrapper():
        input_func()
        input_func()
    
    return wrapper

@run_twice
def write_name():
    print('Erfan')


write_name()

