def my_decorator(input_function):
    def wrapper():
        print('start decorator')
        input_function()
        print('end decorator')
        
    return wrapper

def say_hello():
    print('hello')
    
a = my_decorator(say_hello)
a()
