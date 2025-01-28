print('start')

try:
    print(10/0)
    print(100/user_num)
    import mymodule
    print('second')
    
except ModuleNotFoundError:
    print('This module do not exist')
    
except NameError:
    print('This variable do not define')
    
except ZeroDivisionError:
    print('Numbers can not divide to zero')
    
print('end')
    
    