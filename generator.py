def my_decorator(input_function):
    def wrapper():
        print('start decorator')
        input_function()
        print('end decorator')
        
    return wrapper

@my_decorator
def say_hello():
    print('hello')
    

@my_decorator
def say_gn():
    print('gn')
    
say_hello()
say_gn()
