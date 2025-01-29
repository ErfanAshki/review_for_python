try:
    print(10/0)
except ZeroDivisionError as error:
    print('Exception')
    print(error)


try:
    import moduke
except ModuleNotFoundError as error:
    print('Exception')
    print(error)
    

try:
    print(a+b)
except Exception as error:
    print('Exception')
    print(error)
    
    